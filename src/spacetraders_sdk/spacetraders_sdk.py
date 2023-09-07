from dacite import from_dict, Config
from requests import Response
from spacetraders_sdk.spacetraders_api import SpaceTradersApi
from spacetraders_sdk.spacetraders_enums import FactionSymbol, ContractType, Deposits, ErrorCodes, FactionTraitSymbol, MarketTradeGoodSupply, MarketTransactionType, Produce, ShipCrewRotation, ShipEngineType, ShipFrameType, ShipModuleType, ShipMountType, ShipNavFlightMode, ShipNavStatus, ShipReactorType, ShipRole, ShipType, SurveySize, SystemType, TradeSymbol, WaypointTraitSymbols, WaypointType
from spacetraders_sdk.spacetraders_objects import Agent, Contract, Faction, Ship


class SpaceTradersSDK:
    api: SpaceTradersApi
    dacite_conf: Config
    agent: Agent
    contracts: dict[str, Contract] = {}
    faction: Faction
    ships: dict[str, Ship] = {}

    def __init__(self, token=None) -> None:
        self.api = SpaceTradersApi()
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
                
                self.agent=agent
                self.contracts[contract.id]=contract
                self.ships[ship.symbol]=ship
                self.faction=faction
                
                return token, agent, contract, faction, ship
        return r
