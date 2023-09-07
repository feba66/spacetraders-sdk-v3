import os
from dotenv import find_dotenv,load_dotenv
from requests import Response
from spacetraders_sdk.spacetraders_enums import FactionSymbol
from spacetraders_sdk.spacetraders_sdk import SpaceTradersSDK

def test_register():
    sdk = SpaceTradersSDK()
    r = sdk.register("testfeba10",FactionSymbol.COSMIC)
    print(r)
    if isinstance(r,Response):
        assert r.status_code == 201 or r.status_code == 409
    else:
        assert r[1].credits == 150000
def test_1():
    load_dotenv(find_dotenv(".env"))
    sdk = SpaceTradersSDK()
    sdk.Login(os.getenv("TEST_TOKEN"))
    sdk.get_my_agent()

if __name__ == "__main__":
    test_1()
