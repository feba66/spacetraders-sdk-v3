from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from spacetraders_sdk.spacetraders_enums import (
    ActivityLevel,
    ContractType,
    Deposits,
    FactionSymbol,
    FactionTraitSymbol,
    MarketTradeGoodType,
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
    SupplyLevel,
    SurveySize,
    SystemType,
    TradeSymbol,
    WaypointModifierType,
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
    origin: ShipNavRouteWaypoint


@dataclass
class ShipNav:
    route: ShipNavRoute
    systemSymbol: str
    waypointSymbol: str
    flightMode: ShipNavFlightMode
    status: ShipNavStatus


@dataclass
class Cooldown:
    remainingSeconds: int
    totalSeconds: int
    expiration: Optional[str]
    shipSymbol: str


@dataclass
class Ship:
    symbol: str
    registration: ShipRegistration
    nav: ShipNav
    crew: ShipCrew
    frame: ShipFrame
    reactor: ShipReactor
    engine: ShipEngine
    cooldown: Cooldown
    modules: list[ShipModule]
    mounts: list[ShipMount]
    cargo: ShipCargo
    fuel: ShipFuel


@dataclass
class WaypointOrbital:
    symbol: str


@dataclass
class SystemWaypoint:
    symbol: str
    x: int
    """Relative position of the waypoint on the system's x axis. This is not an absolute position in the universe."""
    y: int
    """Relative position of the waypoint on the system's y axis. This is not an absolute position in the universe."""
    type: WaypointType
    orbitals: list[WaypointOrbital]
    """Waypoints that orbit this waypoint."""
    orbits: Optional[str]
    """The symbol of the parent waypoint, if this waypoint is in orbit around another waypoint. Otherwise this value is undefined."""


@dataclass
class SystemFaction:
    symbol: FactionSymbol


@dataclass
class System:
    symbol: str
    sectorSymbol: str
    x: int
    """Relative position of the system in the sector in the x axis."""
    y: int
    """Relative position of the system in the sector in the y axis."""
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
class WaypointModifier:
    symbol:WaypointModifierType
    name:str
    description:str
@dataclass
class Waypoint:
    symbol: str
    traits: list[WaypointTrait]
    systemSymbol: str
    x: int
    """Relative position of the waypoint on the system's x axis. This is not an absolute position in the universe."""
    y: int
    """Relative position of the waypoint on the system's y axis. This is not an absolute position in the universe."""
    type: WaypointType
    orbitals: list[WaypointOrbital]
    modifiers:Optional[WaypointModifier]
    isUnderConstruction:bool
    orbits: Optional[str]
    """The symbol of the parent waypoint, if this waypoint is in orbit around another waypoint. Otherwise this value is undefined."""
    faction: Optional[WaypointFaction]
    chart: Optional[Chart]


@dataclass
class ShipyardTransaction:
    waypointSymbol: str
    price: int
    agentSymbol: str
    timestamp: str
    shipSymbol: Optional[str]


@dataclass
class ShipyardShipCrew:
    required: int
    capacity: int


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
    crew: ShipyardShipCrew
    supply: SupplyLevel
    activity: Optional[ActivityLevel]


@dataclass
class Shipyard:
    shipTypes: list[ShipType]
    symbol: str
    transactions: Optional[list[ShipyardTransaction]]
    ships: Optional[list[ShipyardShip]]
    modificationsFee: int
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
    type: MarketTradeGoodType
    """The type of trade good (export, import, or exchange)."""
    tradeVolume: int
    """This is the maximum number of units that can be purchased or sold at this market in a single trade for this good. Trade volume also gives an indication of price volatility. A market with a low trade volume will have large price swings, while high trade volume will be more resilient to price changes."""
    symbol: str
    sellPrice: int
    purchasePrice: int
    supply: SupplyLevel
    activity: Optional[ActivityLevel]


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
    connections: list[str]


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
    timestamp: Optional[datetime]  # custom


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


@dataclass
class ConstructionMaterial:
    tradeSymbol: TradeSymbol
    required: int
    fulfilled: int


@dataclass
class Construction:
    symbol: str
    materials: list[ConstructionMaterial]
    isComplete: bool

@dataclass
class SiphonYield:
    symbol:TradeSymbol
    """Symbol of the good that was siphoned."""
    units:int
    """The number of units siphoned that were placed into the ship's cargo hold."""
@dataclass
class Siphon:
    shipSymbol: str
    """Symbol of the ship that executed the siphon."""
    yield_: SiphonYield
    """Yields from the siphon operation."""


class ScannedWaypoint(Waypoint):
    pass
