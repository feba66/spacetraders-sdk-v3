from dacite import from_dict, Config
from requests import Response
from spacetraders_sdk.spacetraders_api import SpaceTradersApi
from spacetraders_sdk.spacetraders_enums import FactionSymbol, ContractType, Deposits, ErrorCodes, FactionTraitSymbol, MarketTradeGoodSupply, MarketTransactionType, Produce, ShipCrewRotation, ShipEngineType, ShipFrameType, ShipModuleType, ShipMountType, ShipNavFlightMode, ShipNavStatus, ShipReactorType, ShipRole, ShipType, SurveySize, SystemType, TradeSymbol, WaypointTraitSymbols, WaypointType
from spacetraders_sdk.spacetraders_objects import Agent, Contract, Faction, Meta, Ship, Waypoint


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
        self.dacite_conf = Config(cast=[FactionSymbol, ContractType, Deposits, ErrorCodes, FactionTraitSymbol, MarketTradeGoodSupply, MarketTransactionType, Produce, ShipCrewRotation, ShipEngineType,
                                  ShipFrameType, ShipModuleType, ShipMountType, ShipNavFlightMode, ShipNavStatus, ShipReactorType, ShipRole, ShipType, SurveySize, SystemType, TradeSymbol, WaypointTraitSymbols, WaypointType])

    def Login(self, token):
        self.api.Login(token)

    def register(self, symbol: str, factionSymbol: FactionSymbol, email: str = None):
        r: Response = self.api.register(symbol, factionSymbol, email)

        if r.status_code == 201:
            data = r.json()
            if "data" in data:
                data = data["data"]
                token: str = data["token"]
                print(f"TOKEN:{token}")
                agent = from_dict(Agent, data["agent"], self.dacite_conf)
                contract = from_dict(Contract, data["contract"], self.dacite_conf)
                faction = from_dict(Faction, data["faction"], self.dacite_conf)
                ship = from_dict(Ship, data["ship"], self.dacite_conf)

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
                agent = from_dict(Agent, data)
                self.agent = agent
                return agent
        return r

    # region system
    def get_waypoints(self, system_symbol: str, page=1, limit=20) -> tuple[list[Waypoint], Meta] | Response:
        r: Response = self.api.get_waypoints(system_symbol, page, limit)
        if r.status_code == 200:
            data = r.json()
            if "meta" in data:
                meta = from_dict(Meta, data["meta"], self.dacite_conf)
            else:
                meta = None
            if "data" in data:
                data = data["data"]
                waypoints = []
                for wp in data:
                    waypoint = from_dict(Waypoint, wp, self.dacite_conf)
                    waypoints.append(waypoint)
                return waypoints, meta
        return r
    # endregion system

    # region ships
    def get_ships(self, page=1, limit=20) -> Response | tuple[list[Ship], Meta]:
        r: Response = self.api.get_ships(page, limit)
        if r.status_code == 200:
            data = r.json()
            if "meta" in data:
                meta = from_dict(Meta, data["meta"], self.dacite_conf)
            else:
                meta = None
            if "data" in data:
                data = data["data"]
                ships = []
                for s in data:
                    ship = from_dict(Ship, s, self.dacite_conf)
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
                meta = from_dict(Meta, data["meta"], self.dacite_conf)
            else:
                meta = None
            if "data" in data:
                data = data["data"]
                contracts = []
                for con in data:
                    contract = from_dict(Contract, con, self.dacite_conf)
                    contracts.append(contract)
                return contracts, meta
        return r

    def accept_contract(self, contract_id: str) -> Response | tuple[Contract, Agent]:
        r: Response = self.api.accept_contract(contract_id)
        if r.status_code == 200:
            data = r.json()
            data = data["data"]
            agent = from_dict(Agent, data["agent"], self.dacite_conf)
            contract = from_dict(Contract, data["contract"], self.dacite_conf)

            return contract, agent
        return r
    # endregion contracts
