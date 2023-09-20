from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from spacetraders_sdk.spacetraders_enums import (
    ContractType,
    Deposits,
    FactionSymbol,
    FactionTraitSymbol,
    MarketTradeGoodSupply,
    MarketTransactionType,
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


@dataclass
class Meta:
    total: int
    page: int
    limit: int


@dataclass
class Agent:
    accountId: str
    symbol: str
    headquarters: str
    credits: int
    startingFaction: str
    shipCount: Optional[int]


@dataclass
class ContractPayment:
    onFulfilled: int
    onAccepted: int


@dataclass
class ContractDeliverGood:
    tradeSymbol: str
    unitsRequired: int
    destinationSymbol: str
    unitsFulfilled: int


@dataclass
class ContractTerms:
    payment: ContractPayment
    deadline: str
    deliver: Optional[list[ContractDeliverGood]]


@dataclass
class Contract:
    id: str
    factionSymbol: str
    type: ContractType
    terms: ContractTerms
    accepted: bool
    fulfilled: bool
    expiration: Optional[str]
    deadlineToAccept: Optional[str]


@dataclass
class FactionTrait:
    symbol: FactionTraitSymbol
    name: str
    description: str


@dataclass
class Faction:
    symbol: FactionSymbol
    headquarters: str
    traits: list[FactionTrait]
    name: str
    description: str
    isRecruiting: bool


@dataclass
class ShipRequirements:
    power: Optional[int]
    crew: Optional[int]
    slots: Optional[int]


@dataclass
class ShipEngine:
    symbol: ShipEngineType
    requirements: ShipRequirements
    name: str
    description: str
    speed: int
    condition: Optional[int]


@dataclass
class ShipReactor:
    symbol: ShipReactorType
    requirements: ShipRequirements
    name: str
    description: str
    powerOutput: int
    condition: Optional[int]


@dataclass
class Consumed:
    amount: int
    timestamp: str


@dataclass
class ShipFuel:
    current: int
    capacity: int
    consumed: Optional[Consumed]


@dataclass
class ShipCargoItem:
    symbol: TradeSymbol
    name: str
    description: str
    units: int


@dataclass
class ShipModule:
    symbol: ShipModuleType
    requirements: ShipRequirements
    name: str
    capacity: Optional[int]
    range: Optional[int]
    description: str


@dataclass
class ShipModificationTransaction:
    waypointSymbol: str
    shipSymbol: str
    tradeSymbol: str
    totalPrice: int
    timestamp: str


@dataclass
class ShipMount:
    symbol: ShipMountType
    name: str
    description: Optional[str]
    strength: Optional[int]
    deposits: Optional[list[Deposits]]
    requirements: ShipRequirements


@dataclass
class ShipCargo:
    units: int
    inventory: list[ShipCargoItem]
    capacity: int


@dataclass
class ShipFrame:
    symbol: ShipFrameType
    moduleSlots: int
    requirements: ShipRequirements
    fuelCapacity: int
    name: str
    description: str
    mountingPoints: int
    condition: Optional[int]


@dataclass
class ShipCrew:
    # The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a civilized waypoint.
    current: int
    required: int
    capacity: int
    rotation: ShipCrewRotation
    morale: int
    wages: int


@dataclass
class ShipRegistration:
    role: ShipRole
    name: str
    factionSymbol: str


@dataclass
class ShipNavRouteWaypoint:
    symbol: str
    systemSymbol: str
    x: int
    y: int
    type: WaypointType


@dataclass
class ShipNavRoute:
    arrival: str
    departureTime: str
    destination: ShipNavRouteWaypoint
    departure: Optional[ShipNavRouteWaypoint]
    """Deprecated. Use origin instead."""
    origin:ShipNavRouteWaypoint


@dataclass
class ShipNav:
    route: ShipNavRoute
    systemSymbol: str
    waypointSymbol: str
    flightMode: ShipNavFlightMode
    status: ShipNavStatus


@dataclass
class Ship:
    symbol: str
    registration: ShipRegistration
    nav: ShipNav
    crew: ShipCrew
    frame: ShipFrame
    reactor: ShipReactor
    engine: ShipEngine
    modules: list[ShipModule]
    mounts: list[ShipMount]
    cargo: ShipCargo
    fuel: ShipFuel


@dataclass
class SystemWaypoint:
    symbol: str
    x: int
    y: int
    type: WaypointType

@dataclass
class SystemFaction:
    symbol:FactionSymbol

@dataclass
class System:
    symbol: str
    sectorSymbol: str
    x: int
    y: int
    type: SystemType
    waypoints: list[SystemWaypoint]
    factions: list[SystemFaction]


@dataclass
class WaypointTrait:
    symbol: WaypointTraitSymbols
    name: str
    description: str


@dataclass
class WaypointFaction:
    symbol: FactionSymbol


@dataclass
class Chart:
    waypointSymbol: Optional[str]
    submittedBy: Optional[str]
    submittedOn: Optional[str]


@dataclass
class WaypointOrbital:
    symbol: str


@dataclass
class Waypoint:
    symbol: str
    traits: list[WaypointTrait]
    systemSymbol: str
    x: int
    y: int
    type: WaypointType
    orbitals: list[WaypointOrbital]
    faction: Optional[WaypointFaction]
    chart: Optional[Chart]


@dataclass
class ShipyardTransaction:
    waypointSymbol:str
    price: int
    agentSymbol: str
    timestamp: str
    shipSymbol: Optional[str]


@dataclass
class ShipyardShip:
    engine: ShipEngine
    reactor: ShipReactor
    name: str
    description: str
    mounts: list[ShipMount]
    purchasePrice: int
    modules: list[ShipModule]
    frame: ShipFrame
    type: Optional[ShipType]


@dataclass
class Shipyard:
    shipTypes: list[ShipType]
    symbol: str
    transactions: Optional[list[ShipyardTransaction]]
    ships: Optional[list[ShipyardShip]]
    modificationsFee:int
    """The fee to modify a ship at this shipyard. This includes installing or removing modules and mounts on a ship. In the case of mounts, the fee is a flat rate per mount. In the case of modules, the fee is per slot the module occupies."""

@dataclass
class TradeGood:
    symbol: TradeSymbol
    name: str
    description: str


@dataclass
class MarketTransaction:
    waypointSymbol: str
    shipSymbol: str
    units: int
    type: MarketTransactionType
    pricePerUnit: int
    timestamp: str
    tradeSymbol: str
    totalPrice: int


@dataclass
class Transaction:
    timestamp: str
    totalPrice: int


@dataclass
class MarketTradeGood:
    tradeVolume: int
    symbol: str
    sellPrice: int
    purchasePrice: int
    supply: MarketTradeGoodSupply


@dataclass
class Market:
    symbol: str
    imports: list[TradeGood]
    exports: list[TradeGood]
    exchange: list[TradeGood]
    transactions: Optional[list[MarketTransaction]]
    tradeGoods: Optional[list[MarketTradeGood]]


@dataclass
class ConnectedSystem:
    symbol: str
    sectorSymbol: str
    distance: int
    x: int
    y: int
    type: SystemType
    factionSymbol: Optional[str]


@dataclass
class JumpGate:
    connectedSystems: list[ConnectedSystem]
    jumpRange: int
    factionSymbol: Optional[str]


@dataclass
class Cooldown:
    remainingSeconds: int
    totalSeconds: int
    expiration: str
    shipSymbol: str


@dataclass
class SurveyDeposit:
    symbol: Deposits


@dataclass
class Survey:
    symbol: str
    size: SurveySize
    signature: str
    expiration: str
    deposits: list[SurveyDeposit]
    timestamp: Optional[datetime] # custom


@dataclass
class ExtractionYield:
    symbol: TradeSymbol
    units: int


@dataclass
class Extraction:
    yield_: ExtractionYield
    shipSymbol: str


@dataclass
class Error:
    message: str
    code: int


@dataclass
class ShipScanFrame:
    symbol: ShipFrameType


@dataclass
class ShipScanReactor:
    symbol: ShipReactorType


@dataclass
class ShipScanEngine:
    symbol: ShipEngineType


@dataclass
class ShipScanMount:
    symbol: ShipMountType


@dataclass
class ScannedShip:
    symbol: str
    registration: ShipRegistration
    nav: ShipNav
    frame: Optional[ShipScanFrame]
    reactor: Optional[ShipScanReactor]
    engine: ShipScanReactor
    mounts: Optional[list[ShipMountType]]


@dataclass
class ScannedSystem:
    symbol: str
    sectorSymbol: str
    x: int
    y: int
    type: SystemType
    distance: int


class ScannedWaypoint(Waypoint):
    pass
