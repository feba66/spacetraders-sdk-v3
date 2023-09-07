
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


if __name__ == "__main__":
    test_register()
