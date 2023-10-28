import os
from pprint import pprint
from dotenv import find_dotenv, load_dotenv
from spacetraders_sdk.spacetraders_api import SpaceTradersApi
from spacetraders_sdk.spacetraders_enums import WaypointTraitSymbols, WaypointType
from spacetraders_sdk.spacetraders_objects import WaypointTrait


def test_status():
    load_dotenv(find_dotenv(".env"))
    st = SpaceTradersApi(os.getenv("SERVERURL"))
    status = st.status()
    assert status != None
    assert status.text != None


def test_waypoints():
    load_dotenv(find_dotenv(".env"))
    st = SpaceTradersApi(os.getenv("SERVERURL"))
    st.Login(os.getenv("TOKEN"))
    ships = st.get_ships().json()["data"]
    print(ships)
    waypoints = st.get_waypoints(ships[0]["nav"]["systemSymbol"], traits=WaypointTraitSymbols.THIN_ATMOSPHERE)
    pprint(waypoints.json())
    assert waypoints != None
    assert waypoints.text != None


def test_waypoints2():
    load_dotenv(find_dotenv(".env"))
    st = SpaceTradersApi(os.getenv("SERVERURL"))
    st.Login(os.getenv("TOKEN"))
    ships = st.get_ships().json()["data"]
    print(ships)
    waypoints = st.get_waypoints(ships[0]["nav"]["systemSymbol"], type=WaypointType.ASTEROID_BASE)
    pprint(waypoints.json())
    assert waypoints != None
    assert waypoints.text != None


test_waypoints()
