from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from spacetraders_sdk.spacetraders_enums import (
    ContractType,
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
    terms: ContractTerms
    factionSymbol: str
    fulfilled: bool
    accepted: bool
    expiration: Optional[str]
    deadlineToAccept: Optional[str]
    id: str
    type: ContractType


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
    power: int
    crew: int
    slots: int


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
    consumed: Consumed


@dataclass
class ShipCargoItem:
    symbol: str
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
    description: Optional[str]


@dataclass
class ShipMount:
    symbol: ShipMountType
    requirements: ShipRequirements
    name: str
    description: Optional[str]
    strength: Optional[int]


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
    wages: int
    current: int
    rotation: ShipCrewRotation
    morale: int
    required: int
    capacity: int


@dataclass
class ShipRegistration:
    role: str
    name: str
    factionSymbol: Optional[str]


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
    departure: ShipNavRouteWaypoint


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
    nav: ShipNav
    engine: ShipEngine
    fuel: ShipFuel
    reactor: ShipReactor
    mounts: list[ShipMount]
    registration: ShipRegistration
    cargo: ShipCargo
    modules: list[ShipModule]
    crew: ShipCrew
    frame: ShipFrame


@dataclass
class SystemWaypoint:
    symbol: str
    x: int
    y: int
    type: WaypointType


@dataclass
class System:
    symbol: str
    sectorSymbol: str
    x: int
    y: int
    type: SystemType
    waypoints: list[SystemWaypoint]
    factions: list[str]


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


@dataclass
class TradeGood:
    symbol: TradeSymbol
    name: str
    description: str


@dataclass
class MarketTransaction:
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
    distance: int
    sectorSymbol: str
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
    expiredAt: Optional[str]


@dataclass
class SurveyDeposit:
    symbol: str


@dataclass
class Survey:
    symbol: str
    size: SurveySize
    signature: str
    expiration: str
    deposits: list[SurveyDeposit]
    timestamp: Optional[datetime]


@dataclass
class ExtractionYield:
    symbol: str
    units: int


@dataclass
class Extraction:
    yield_: ExtractionYield
    shipSymbol: str


@dataclass
class Error:
    message: str
    code: int
