import os
from pprint import pprint
from dotenv import find_dotenv, load_dotenv
from requests import Response
from spacetraders_sdk.spacetraders_enums import FactionSymbol, WaypointTraitSymbols, WaypointType
from spacetraders_sdk.spacetraders_sdk import SpaceTradersSDK
import random
import string


def test_register():
    load_dotenv(find_dotenv(".env"))
    sdk = SpaceTradersSDK(os.getenv("SERVERURL"))
    userappendix = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    r = sdk.register("FEBATST"+userappendix, FactionSymbol.COSMIC)
    print(r)
    if isinstance(r, Response):
        assert r.status_code == 201 or r.status_code == 409
    else:
        assert r[1].credits >= 0


def test_get_contracts():
    load_dotenv(find_dotenv(".env"))
    sdk = SpaceTradersSDK(os.getenv("SERVERURL"))
    sdk.Login(os.getenv("TOKEN"))
    print(sdk.get_contracts())


def test_accept_contracts():
    load_dotenv(find_dotenv(".env"))
    sdk = SpaceTradersSDK(os.getenv("SERVERURL"))
    sdk.Login(os.getenv("TOKEN"))
    cl, m = sdk.get_contracts()
    print(sdk.accept_contract(cl[0].id))


def test_1():
    load_dotenv(find_dotenv(".env"))
    sdk = SpaceTradersSDK(os.getenv("SERVERURL"))
    sdk.Login(os.getenv("TOKEN"))
    # sdk.get_my_agent()
    # print(sdk.get_waypoints("X1-V94"))
    print(sdk.get_ships())


def test_status():
    load_dotenv(find_dotenv(".env"))
    sdk = SpaceTradersSDK(os.getenv("SERVERURL"))
    print(sdk.api.status().json())


def resulter(r):
    pprint(r)
    try:
        print(r.json())
    except:
        pass


if __name__ == "__main__":
    test_register()
    exit()
    load_dotenv(find_dotenv(".env"))
    sdk = SpaceTradersSDK(os.getenv("SERVERURL"))
    sdk.Login(os.getenv("TOKEN"))
    # r = sdk.api.my_req("/systems/X1-RF46/waypoints/X1-RF46-I58/construction","get")
    # print(r)
    # print(r.json())
    # a = sdk.get_my_agent()
    # r = sdk.get_waypoints(a.headquarters.rsplit("-",1)[0],type=WaypointType.JUMP_GATE)
    # r = sdk.api.get_construction("X1-JN57-I55")
    # r = sdk.get_contracts()
    # r = sdk.get_waypoints("X1-CP67", traits=[WaypointTraitSymbols.COMMON_METAL_DEPOSITS, WaypointTraitSymbols.STRIPPED])
    # r = sdk.accept_contract(r[0][0].id)

    ships, m = sdk.get_ships()

    market = sdk.get_market(ships[0].nav.waypointSymbol)

    pprint(market)
