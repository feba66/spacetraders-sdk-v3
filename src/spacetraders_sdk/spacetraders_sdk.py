from dacite import from_dict, Config
from requests import Response
from spacetraders_sdk.spacetraders_api import SpaceTradersApi
from spacetraders_sdk.spacetraders_enums import FactionSymbol, ContractType, WaypointModifierType, Deposits, ErrorCodes, FactionTraitSymbol, SupplyLevel, ActivityLevel, MarketTransactionType, Produce, ShipCrewRotation, ShipEngineType, ShipFrameType, ShipModuleType, ShipMountType, ShipNavFlightMode, ShipNavStatus, ShipReactorType, ShipRole, ShipType, SurveySize, SystemType, TradeSymbol, WaypointTraitSymbols, WaypointType
from spacetraders_sdk.spacetraders_objects import Agent, Contract, Faction, Meta, Ship, Waypoint, WaypointTrait


class SpaceTradersSDK:
    api: SpaceTradersApi
    dacite_conf: Config
    agent: Agent
    contracts: dict[str, Contract] = {}
    faction: Faction
    ships: dict[str, Ship] = {}

    def __init__(self, url="https://api.spacetraders.io/v2", token=None) -> None:
        self.api = SpaceTradersApi(url=url)
        if token:
            self.api.Login(token)
        self.dacite_conf = Config(cast=[FactionSymbol, ContractType, Deposits, ErrorCodes, FactionTraitSymbol, SupplyLevel, ActivityLevel, MarketTransactionType, Produce, ShipCrewRotation, ShipEngineType,
                                  ShipFrameType, WaypointModifierType, ShipModuleType, ShipMountType, ShipNavFlightMode, ShipNavStatus, ShipReactorType, ShipRole, ShipType, SurveySize, SystemType, TradeSymbol, WaypointTraitSymbols, WaypointType])
    
    def Login(self, token):
        self.api.Login(token)

    def conv(self,cls,obj):
        return from_dict(cls,obj,self.dacite_conf)
    
    # region Agents
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

    def get_waypoints(self, system_symbol: str, page=1, limit=20, type: WaypointType = None, traits: WaypointTraitSymbols | list[WaypointTraitSymbols] = None) -> tuple[list[Waypoint], Meta] | Response:
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
    # endregion system
    # region Contracts
    def get_contracts(self, page=1, limit=20):
        r = self.api.get_contracts(page,limit)

        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                contracts = [self.conv(Contract, d) for d in data["data"]]
                for c in contracts:
                    self.contracts[c.id]=c
                return contracts
        return r

    def get_contract(self, contract_id: str):
        r = self.api.get_contract(contract_id)

        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                c = self.conv(Contract, data["data"])
                self.contracts[c.id]=c
                return c
        return r

    def accept_contract(self, contract_id: str):
        r = self.api.accept_contract(contract_id)

        if r.status_code == 200:
            data = r.json()
            if "data" in data:
                agent = self.conv(Agent, data["data"]["agent"])
                c = self.conv(Contract, data["data"]["contract"])
                self.contracts[c.id]=c
                self.agent=agent
                return c,agent
        return r

    def deliver_contract(self, contract_id: str, ship_symbol: str, trade_symbol: str, units: int):
        path = f"/my/contracts/{contract_id}/deliver"
        r = self.my_req(path, "post", data={"shipSymbol": ship_symbol, "tradeSymbol": trade_symbol, "units": units})
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
                return ships, meta
        return r

    def navigate(self, ship: Ship | str, waypoint: str):
        r: Response = self.api.navigate(ship if isinstance(ship, str) else ship.symbol, waypoint)
        # wip
        return r
    # endregion ships

    # region contracts
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

    def accept_contract(self, contract_id: str) -> Response | tuple[Contract, Agent]:
        r: Response = self.api.accept_contract(contract_id)
        if r.status_code == 200:
            data = r.json()
            data = data["data"]
            agent = self.conv(Agent, data["agent"])
            contract = self.conv(Contract, data["contract"])

            return contract, agent
        return r
    # endregion contracts
