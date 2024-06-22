from dacite import from_dict, Config
from requests import Response
from spacetraders_sdk.spacetraders_api import SpaceTradersApi
from spacetraders_sdk.spacetraders_enums import (
    FactionSymbol,
    ContractType,
    MarketTradeGoodType,
    WaypointModifierType,
    Deposits,
    ErrorCodes,
    FactionTraitSymbol,
    SupplyLevel,
    ActivityLevel,
    MarketTransactionType,
    Produce,
    ShipCrewRotation,
    ShipEngineType,
    ShipFrameType,
    ShipModuleType,
    ShipMountType,
    ShipNavFlightMode,
    ShipNavStatus,
    ShipReactorType,
    ShipRole,
    ShipType,
    SurveySize,
    SystemType,
    TradeSymbol,
    WaypointTraitSymbols,
    WaypointType,
)
from spacetraders_sdk.spacetraders_objects import (
    Agent,
    Construction,
    Contract,
    Cooldown,
    Extraction,
    Faction,
    JumpGate,
    Market,
    MarketTransaction,
    Meta,
    Ship,
    ShipCargo,
    ShipFuel,
    ShipNav,
    Shipyard,
    Siphon,
    Waypoint,
)


class SpaceTradersSDK:
    api: SpaceTradersApi
    dacite_conf: Config
    agent: Agent
    contracts: dict[str, Contract] = {}
    faction: Faction
    ships: dict[str, Ship] = {}
    markets: dict[str, Market] = {}
    shipyards: dict[str, Shipyard] = {}
    jumpgates: dict[str, JumpGate] = {}
    constructions: dict[str, Construction] = {}

    def __init__(self, url="https://api.spacetraders.io/v2", token=None) -> None:
        self.api = SpaceTradersApi(url=url)
        if token:
            self.api.Login(token)
        self.dacite_conf = Config(
            cast=[
                FactionSymbol,
                ContractType,
                Deposits,
                ErrorCodes,
                FactionTraitSymbol,
                SupplyLevel,
                ActivityLevel,
                MarketTransactionType,
                Produce,
                ShipCrewRotation,
                ShipEngineType,
                ShipFrameType,
                MarketTradeGoodType,
                WaypointModifierType,
                ShipModuleType,
                ShipMountType,
                ShipNavFlightMode,
                ShipNavStatus,
                ShipReactorType,
                ShipRole,
                ShipType,
                SurveySize,
                SystemType,
                TradeSymbol,
                WaypointTraitSymbols,
                WaypointType,
            ]
        )

    def conv(self, cls, obj):
        return from_dict(cls, obj, self.dacite_conf)

    # region Account
    def Login(self, token):
        self.api.Login(token)

    def register(self, symbol: str, factionSymbol: FactionSymbol, email: str = None):
        r: Response = self.api.register(symbol, factionSymbol, email)

        if r.status_code == 201:
            data = r.json()
            if "data" in data:
                data = data["data"]
                token: str = data["token"]
                self.api.logger.info(f"TOKEN:{token}")
                agent = self.conv(Agent, data["agent"])
                contract = self.conv(Contract, data["contract"])
                faction = self.conv(Faction, data["faction"])
                ship = self.conv(Ship, data["ship"])

                self.agent = agent
                self.contracts[contract.id] = contract
                self.ships[ship.symbol] = ship
                self.faction = faction

                return token, agent, contract, faction, ship
        return r

    # endregion Account
    # region Agents

    def get_my_agent(self):
        r = self.api.get_my_agent()

        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                agent = self.conv(Agent, data)
                self.agent = agent
                return agent
        return r

    def get_agents(self, page=1, limit=20):
        r = self.api.get_agents(page, limit)

        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                agents = [self.conv(Agent, d) for d in data]
                return agents
        return r

    def get_agent(self, agent_symbol: str):
        r = self.api.get_agent(agent_symbol)

        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                agent = self.conv(Agent, data)
                return agent
        return r

    # endregion Agents
    # region system

    def get_waypoints(
        self,
        system_symbol: str,
        page=1,
        limit=20,
        type: WaypointType = None,
        traits: WaypointTraitSymbols | list[WaypointTraitSymbols] = None,
    ) -> tuple[list[Waypoint], Meta] | Response:
        r: Response = self.api.get_waypoints(system_symbol, page, limit, type, traits)
        if r.status_code == 200:
            data = r.json()
            if "meta" in data:
                meta = self.conv(Meta, data["meta"])
            else:
                meta = None
            if "data" in data:
                data = data["data"]
                waypoints = []
                for wp in data:
                    waypoint = self.conv(Waypoint, wp)
                    waypoints.append(waypoint)
                return waypoints, meta
        return r

    def get_market(self, waypoint_symbol: str | Waypoint):
        r: Response = self.api.get_market(
            waypoint_symbol
            if isinstance(waypoint_symbol, str)
            else waypoint_symbol.symbol
        )
        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                market = self.conv(Market, data)
                self.markets[
                    (
                        waypoint_symbol
                        if isinstance(waypoint_symbol, str)
                        else waypoint_symbol.symbol
                    )
                ] = market
                return market
        return r

    def get_shipyard(self, waypoint_symbol: str | Waypoint):
        r: Response = self.api.get_shipyard(
            waypoint_symbol
            if isinstance(waypoint_symbol, str)
            else waypoint_symbol.symbol
        )
        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                shipyard = self.conv(Shipyard, data)
                self.shipyards[
                    (
                        waypoint_symbol
                        if isinstance(waypoint_symbol, str)
                        else waypoint_symbol.symbol
                    )
                ] = shipyard
                return shipyard
        return r

    def get_jumpgate(self, waypoint_symbol: str):
        r: Response = self.api.get_jumpgate(waypoint_symbol)
        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                jumpgate = self.conv(JumpGate, data)
                self.jumpgates[waypoint_symbol] = jumpgate
                return jumpgate
        return r

    def get_construction(self, waypoint_symbol: str):
        """Get construction details for a waypoint. Requires a waypoint with a property of `isUnderConstruction` to be true."""
        r: Response = self.api.get_construction(waypoint_symbol)
        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                construction = self.conv(Construction, data)
                self.constructions[waypoint_symbol] = construction
                return construction
        return r

    # endregion system
    # region Contracts

    def get_contracts(self, page=1, limit=20) -> Response | tuple[list[Contract], Meta]:
        r: Response = self.api.get_contracts(page, limit)
        if r.status_code == 200:
            data = r.json()
            if "meta" in data:
                meta = self.conv(Meta, data["meta"])
            else:
                meta = None
            if "data" in data:
                data = data["data"]
                contracts = []
                for con in data:
                    contract = self.conv(Contract, con)
                    contracts.append(contract)
                return contracts, meta
        return r

    def get_contract(self, contract_id: str):
        r = self.api.get_contract(contract_id)

        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                c = self.conv(Contract, data["data"])
                self.contracts[c.id] = c
                return c
        return r

    def accept_contract(self, contract_id: str):
        r = self.api.accept_contract(contract_id)

        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                agent = self.conv(Agent, data["data"]["agent"])
                c = self.conv(Contract, data["data"]["contract"])
                self.contracts[c.id] = c
                self.agent = agent
                return c, agent
        return r

    def deliver_contract(
        self, contract_id: str, ship_symbol: str, trade_symbol: str, units: int
    ):
        path = f"/my/contracts/{contract_id}/deliver"
        r = self.my_req(
            path,
            "post",
            data={
                "shipSymbol": ship_symbol,
                "tradeSymbol": trade_symbol,
                "units": units,
            },
        )
        return r

    def fulfill_contract(self, contract_id: str):
        path = f"/my/contracts/{contract_id}/fulfill"
        r = self.my_req(path, "post")
        return r

    # endregion
    # region ships
    def get_ships(self, page=1, limit=20) -> Response | tuple[list[Ship], Meta]:
        r: Response = self.api.get_ships(page, limit)
        if r.status_code == 200:
            data = r.json()
            if "meta" in data:
                meta = self.conv(Meta, data["meta"])
            else:
                meta = None
            if "data" in data:
                data = data["data"]
                ships = []
                for s in data:
                    ship = self.conv(Ship, s)
                    ships.append(ship)
                    self.ships[ship.symbol] = ship
                return ships, meta
        return r

    def get_ship(self, ship: Ship | str) -> Response | Ship:
        r: Response = self.api.get_ship(ship if isinstance(ship, str) else ship.symbol)
        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                s = self.conv(Ship, data)
                self.ships[s.symbol]
                return s
        return r

    def navigate(self, ship: Ship | str, waypoint: str):
        r: Response = self.api.navigate(
            ship if isinstance(ship, str) else ship.symbol, waypoint
        )
        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                fuel = self.conv(ShipFuel, data["fuel"])
                nav = self.conv(ShipNav, data["nav"])
                self.ships[ship if isinstance(ship, str) else ship.symbol].fuel = fuel
                self.ships[ship if isinstance(ship, str) else ship.symbol].nav = nav
                return fuel, nav
        return r

    def orbit(self, ship: Ship | str):
        ship_symbol = ship if isinstance(ship, str) else ship.symbol
        r: Response = self.api.orbit(ship_symbol)
        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                nav = self.conv(ShipNav, data["nav"])
                if ship_symbol in self.ships:
                    self.ships[ship_symbol].nav = nav
                return nav
        return r

    def dock(self, ship: Ship | str):
        r: Response = self.api.dock(ship if isinstance(ship, str) else ship.symbol)
        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                nav = self.conv(ShipNav, data["nav"])
                self.ships[ship if isinstance(ship, str) else ship.symbol].nav = nav
                return nav
        return r

    def refuel(self, ship: Ship | str, fuel_units: int):
        r: Response = self.api.refuel(
            ship if isinstance(ship, str) else ship.symbol, fuel_units
        )
        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                agent = self.conv(Agent, data["agent"])
                fuel = self.conv(ShipFuel, data["fuel"])
                transaction = self.conv(MarketTransaction, data["transaction"])
                self.ships[ship if isinstance(ship, str) else ship.symbol].fuel = fuel
                self.agent = agent
                return agent, fuel, transaction
        return r

    def sell(self, ship: Ship | str, symbol: str, units: int):
        r: Response = self.api.sell(
            ship if isinstance(ship, str) else ship.symbol, symbol, units
        )
        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                agent = self.conv(Agent, data["agent"])
                cargo = self.conv(ShipCargo, data["cargo"])
                transaction = self.conv(MarketTransaction, data["transaction"])
                self.ships[ship if isinstance(ship, str) else ship.symbol].cargo = cargo
                self.agent = agent
                return agent, cargo, transaction
        return r

    def purchase(self, ship: Ship | str, symbol: str, units: int):
        r: Response = self.api.purchase(
            ship if isinstance(ship, str) else ship.symbol, symbol, units
        )
        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                data = data["data"]
                agent = self.conv(Agent, data["agent"])
                cargo = self.conv(ShipCargo, data["cargo"])
                transaction = self.conv(MarketTransaction, data["transaction"])
                self.ships[ship if isinstance(ship, str) else ship.symbol].cargo = cargo
                self.agent = agent
                return agent, cargo, transaction
        return r

    def extract(self, ship: Ship | str):
        r: Response = self.api.extract(ship if isinstance(ship, str) else ship.symbol)
        if r.status_code == 201:
            data = r.json()
            if "data" in data:
                data = data["data"]
                cooldown = self.conv(Cooldown, data["cooldown"])
                extraction = self.conv(Extraction, data["extraction"])
                cargo = self.conv(ShipCargo, data["cargo"])
                self.ships[ship if isinstance(ship, str) else ship.symbol].cargo = cargo
                self.ships[ship if isinstance(ship, str) else ship.symbol].cooldown = (
                    cooldown
                )
                return cooldown, extraction, cargo
        return r

    def extract_with_survey(self, ship: Ship | str, survey: dict):
        r: Response = self.api.extract_with_survey(
            ship if isinstance(ship, str) else ship.symbol, survey
        )
        if r.status_code == 201:
            data = r.json()
            if "data" in data:
                data = data["data"]
                cooldown = self.conv(Cooldown, data["cooldown"])
                extraction = self.conv(Extraction, data["extraction"])
                cargo = self.conv(ShipCargo, data["cargo"])
                self.ships[ship if isinstance(ship, str) else ship.symbol].cargo = cargo
                self.ships[ship if isinstance(ship, str) else ship.symbol].cooldown = (
                    cooldown
                )
                return cooldown, extraction, cargo
        return r

    def siphon(self, ship: Ship | str):
        r: Response = self.api.siphon(ship if isinstance(ship, str) else ship.symbol)
        if r.status_code == 201:
            data = r.json()
            if "data" in data:
                data = data["data"]
                cooldown = self.conv(Cooldown, data["cooldown"])
                siphon = self.conv(Siphon, data["siphon"])
                cargo = self.conv(ShipCargo, data["cargo"])
                self.ships[ship if isinstance(ship, str) else ship.symbol].cargo = cargo
                self.ships[ship if isinstance(ship, str) else ship.symbol].cooldown = (
                    cooldown
                )
                return cooldown, siphon, cargo
        return r

    # endregion ships
