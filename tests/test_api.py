from spacetraders_sdk.spacetraders_api import SpaceTradersApi

def test_status():
    st = SpaceTradersApi()
    status = st.status()
    assert status != None
    assert status.text != None