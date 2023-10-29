### New rewrite/repaste

Work in progress... Names may change a lot...

Most endpoints are already in, but you have to handle the data yourself (for now).


### TODO
- Data Classes (Pydantic or from a db scheme directly)
- Database
- Sdk Statekeeping

### Code

Api usage:

~~~py
from spacetraders_sdk.spacetraders_api import SpaceTradersApi

st = SpaceTradersApi()
status = st.status()
~~~


### Documentation for API Endpoints

Class          | HTTP request  | Description   | Implemented
------------   | ------------- | ------------- | -------------
|              | **get** /     | Status        | api
|              | **post** /register | Register New Agent | api & sdk
| *Agents*     | **get** /my/agent | Fetch your agent's details. | api & sdk
| *Agents*     | **get** /agents | List all Agents. | api
| *Agents*     | **get** /agents/{agent_symbol} | Get Agent. | api
| *Contracts*  | **get** /my/contracts | List all of your contracts. | api
| *Contracts*  | **get** /my/contracts/{contractId} | Get the details of a contract by ID. | api
| *Contracts*  | **post** /my/contracts/{contractId}/accept | Accept a contract. | api
| *Contracts*  | **post** /my/contracts/{contractId}/deliver | Deliver cargo on a given contract. |  api
| *Contracts*  | **post** /my/contracts/{contractId}/fulfill | Fulfill a contract | api
| *Factions*   | **get** /factions | List all discovered factions in the game. |  api
| *Factions*   | **get** /factions/{factionSymbol} | View the details of a faction. |  api
| *Fleet*      | **get** /my/ships | Retrieve all of your ships. |  api & sdk
| *Fleet*      | **post** /my/ships | Purchase a ship |  api
| *Fleet*      | **get** /my/ships/{shipSymbol} | Retrieve the details of your ship. |   api
| *Fleet*      | **get** /my/ships/{shipSymbol}/cargo | Retrieve the cargo of your ship. |   api
| *Fleet*      | **post** /my/ships/{shipSymbol}/orbit | Orbit Ship |  api
| *Fleet*      | **post** /my/ships/{shipSymbol}/refine | Ship Refine | api
| *Fleet*      | **post** /my/ships/{shipSymbol}/chart | Create Chart |  api
| *Fleet*      | **get** /my/ships/{shipSymbol}/cooldown | Get Ship Cooldown | api
| *Fleet*      | **post** /my/ships/{shipSymbol}/dock | Dock Ship |  api
| *Fleet*      | **post** /my/ships/{shipSymbol}/survey | Create Survey | api
| *Fleet*      | **post** /my/ships/{shipSymbol}/extract | Extract Resources |  api
| *Fleet*      | **post** /my/ships/{shipSymbol}/extract/survey | Extract Resources with Survey |  api
| *Fleet*      | **post** /my/ships/{shipSymbol}/siphon | Siphon Resources | api
| *Fleet*      | **post** /my/ships/{shipSymbol}/jettison | Jettison Cargo | api
| *Fleet*      | **post** /my/ships/{shipSymbol}/jump | Jump Ship |  api
| *Fleet*      | **post** /my/ships/{shipSymbol}/navigate | Navigate Ship |  api
| *Fleet*      | **post** /my/ships/{shipSymbol}/negotiate/contract | Negotiate Contract | api
| *Fleet*      | **patch** /my/ships/{shipSymbol}/nav | Patch Ship Nav | api
| *Fleet*      | **get** /my/ships/{shipSymbol}/nav | Get Ship Nav | api
| *Fleet*      | **post** /my/ships/{shipSymbol}/warp | Warp Ship |  api
| *Fleet*      | **post** /my/ships/{shipSymbol}/sell | Sell Cargo |  api
| *Fleet*      | **post** /my/ships/{shipSymbol}/scan/systems | Scan Systems | api
| *Fleet*      | **post** /my/ships/{shipSymbol}/scan/waypoints | Scan Waypoints | api
| *Fleet*      | **post** /my/ships/{shipSymbol}/scan/ships | Scan Ships | api
| *Fleet*      | **post** /my/ships/{shipSymbol}/refuel | Refuel Ship |  api
| *Fleet*      | **post** /my/ships/{shipSymbol}/purchase | Purchase Cargo |  api
| *Fleet*      | **post** /my/ships/{shipSymbol}/transfer | Transfer Cargo |  api
| *Fleet*      | **get** /my/ships/{shipSymbol}/mounts | Get the mounts on a ship. | api
| *Fleet*      | **post** /my/ships/{shipSymbol}/mounts | Install a mount on a ship. | api
| *Fleet*      | **post** /my/ships/{shipSymbol}/mounts/remove | Remove a mount from a ship. | api
| *Systems*    | **get** /systems | List Systems |  api
| *Systems*    | **get** /systems.json | Get all systems. |   api
| *Systems*    | **get** /systems/{systemSymbol} | Get System |  api
| *Systems*    | **get** /systems/{systemSymbol}/waypoints | List Waypoints |  api & sdk
| *Systems*    | **get** /systems/{systemSymbol}/waypoints/{waypointSymbol} | Get Waypoint |  api
| *Systems*    | **get** /systems/{systemSymbol}/waypoints/{waypointSymbol}/market | Get Market |  api
| *Systems*    | **get** /systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard | Get Shipyard |  api
| *Systems*    | **get** /systems/{systemSymbol}/waypoints/{waypointSymbol}/jump-gate | Get Jump Gate | api
| *Systems*    | **get** /systems/{systemSymbol}/waypoints/{waypointSymbol}/construction | Get Construction Site | api
| *Systems*    | **post** /systems/{systemSymbol}/waypoints/{waypointSymbol}/construction/supply | Supply Construction Site | api


api: 52/52


Completed Objects:
- Agent
- Chart
- ConnectedSystem
- Contract
- Cooldown
- Extraction
- Faction
- JumpGate
- Market
- ScannedShip
- ScannedSystem
- ScannedWaypoint
- Ship
- ShipCondition -> int
- Shipyard
- Survey
- System
- TradeSymbol
- Waypoint


~~~py
poetry add [-dev] <dependency>
poetry install
poetry build
~~~
