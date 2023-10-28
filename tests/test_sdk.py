import os
from dotenv import find_dotenv, load_dotenv
from requests import Response
from spacetraders_sdk.spacetraders_enums import FactionSymbol
from spacetraders_sdk.spacetraders_sdk import SpaceTradersSDK


def test_register():
    load_dotenv(find_dotenv(".env"))
    sdk = SpaceTradersSDK(os.getenv("SERVERURL"))
    r = sdk.register("testfeba11", FactionSymbol.COSMIC)
    print(r)
    if isinstance(r, Response):
        assert r.status_code == 201 or r.status_code == 409
    else:
        assert r[1].credits == 150000


def test_get_contracts():
    load_dotenv(find_dotenv(".env"))
    sdk = SpaceTradersSDK(os.getenv("SERVERURL"))
    sdk.Login(os.getenv("TOKEN"))
    print(sdk.get_contracts())

def test_accept_contracts():
    load_dotenv(find_dotenv(".env"))
    sdk = SpaceTradersSDK(os.getenv("SERVERURL"))
    sdk.Login(os.getenv("TOKEN"))
    cl,m = sdk.get_contracts()
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


if __name__ == "__main__":
    test_get_contracts()
