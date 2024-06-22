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

| Class       | HTTP request                                                                    | Description                               | api | sdk |
| ----------- | ------------------------------------------------------------------------------- | ----------------------------------------- | --- | --- |
|             | **get**  /                                                                      | Status                                    | [x] | [ ] |
|             | **post** /register                                                              | Register New Agent                        | [x] | [x] |
| *Agents*    | **get**  /my/agent                                                              | Fetch your agent's details.               | [x] | [x] |
| *Agents*    | **get**  /agents                                                                | List all Agents.                          | [x] | [x] |
| *Agents*    | **get**  /agents/{agent_symbol}                                                 | Get Agent.                                | [x] | [x] |
| *Contracts* | **get**  /my/contracts                                                          | List all of your contracts.               | [x] | [x] |
| *Contracts* | **get**  /my/contracts/{contractId}                                             | Get the details of a contract by ID.      | [x] | [ ] |
| *Contracts* | **post** /my/contracts/{contractId}/accept                                      | Accept a contract.                        | [x] | [x] |
| *Contracts* | **post** /my/contracts/{contractId}/deliver                                     | Deliver cargo on a given contract.        | [x] | [ ] |
| *Contracts* | **post** /my/contracts/{contractId}/fulfill                                     | Fulfill a contract                        | [x] | [ ] |
| *Factions*  | **get**  /factions                                                              | List all discovered factions in the game. | [x] | [ ] |
| *Factions*  | **get**  /factions/{factionSymbol}                                              | View the details of a faction.            | [x] | [ ] |
| *Fleet*     | **get**  /my/ships                                                              | Retrieve all of your ships.               | [x] | [x] |
| *Fleet*     | **post** /my/ships                                                              | Purchase a ship                           | [x] | [ ] |
| *Fleet*     | **get**  /my/ships/{shipSymbol}                                                 | Retrieve the details of your ship.        | [x] | [x] |
| *Fleet*     | **get**  /my/ships/{shipSymbol}/cargo                                           | Retrieve the cargo of your ship.          | [x] | [ ] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/orbit                                           | Orbit Ship                                | [x] | [x] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/refine                                          | Ship Refine                               | [x] | [ ] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/chart                                           | Create Chart                              | [x] | [ ] |
| *Fleet*     | **get**  /my/ships/{shipSymbol}/cooldown                                        | Get Ship Cooldown                         | [x] | [ ] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/dock                                            | Dock Ship                                 | [x] | [x] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/survey                                          | Create Survey                             | [x] | [ ] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/extract                                         | Extract Resources                         | [x] | [x] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/extract/survey                                  | Extract Resources with Survey             | [x] | [x] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/siphon                                          | Siphon Resources                          | [x] | [x] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/jettison                                        | Jettison Cargo                            | [x] | [ ] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/jump                                            | Jump Ship                                 | [x] | [ ] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/navigate                                        | Navigate Ship                             | [x] | [x] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/negotiate/contract                              | Negotiate Contract                        | [x] | [ ] |
| *Fleet*     | **patch** /my/ships/{shipSymbol}/nav                                            | Patch Ship Nav                            | [x] | [ ] |
| *Fleet*     | **get**  /my/ships/{shipSymbol}/nav                                             | Get Ship Nav                              | [x] | [ ] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/warp                                            | Warp Ship                                 | [x] | [ ] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/sell                                            | Sell Cargo                                | [x] | [x] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/scan/systems                                    | Scan Systems                              | [x] | [ ] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/scan/waypoints                                  | Scan Waypoints                            | [x] | [ ] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/scan/ships                                      | Scan Ships                                | [x] | [ ] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/refuel                                          | Refuel Ship                               | [x] | [x] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/purchase                                        | Purchase Cargo                            | [x] | [x] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/transfer                                        | Transfer Cargo                            | [x] | [ ] |
| *Fleet*     | **get**  /my/ships/{shipSymbol}/mounts                                          | Get the mounts on a ship.                 | [x] | [ ] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/mounts                                          | Install a mount on a ship.                | [x] | [ ] |
| *Fleet*     | **post** /my/ships/{shipSymbol}/mounts/remove                                   | Remove a mount from a ship.               | [x] | [ ] |
| *Systems*   | **get**  /systems                                                               | List Systems                              | [x] | [ ] |
| *Systems*   | **get**  /systems.json                                                          | Get all systems.                          | [x] | [ ] |
| *Systems*   | **get**  /systems/{systemSymbol}                                                | Get System                                | [x] | [ ] |
| *Systems*   | **get**  /systems/{systemSymbol}/waypoints                                      | List Waypoints                            | [x] | [x] |
| *Systems*   | **get**  /systems/{systemSymbol}/waypoints/{waypointSymbol}                     | Get Waypoint                              | [x] | [ ] |
| *Systems*   | **get**  /systems/{systemSymbol}/waypoints/{waypointSymbol}/market              | Get Market                                | [x] | [x] |
| *Systems*   | **get**  /systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard            | Get Shipyard                              | [x] | [x] |
| *Systems*   | **get**  /systems/{systemSymbol}/waypoints/{waypointSymbol}/jump-gate           | Get Jump Gate                             | [x] | [x] |
| *Systems*   | **get**  /systems/{systemSymbol}/waypoints/{waypointSymbol}/construction        | Get Construction Site                     | [x] | [x] |
| *Systems*   | **post** /systems/{systemSymbol}/waypoints/{waypointSymbol}/construction/supply | Supply Construction Site                  | [x] | [ ] |


api: 52/52
sdk 22/52

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
