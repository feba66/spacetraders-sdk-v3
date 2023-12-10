
from dacite import from_dict
import dacite
from spacetraders_sdk.spacetraders_objects import Faction
from spacetraders_sdk.spacetraders_enums import FactionSymbol


def test_enum_dacite():
    conf = dacite.Config(cast=[FactionSymbol])
    f = from_dict(Faction, {"symbol": "ASTRO", "headquarters": "X1-ABC12-ABC123", "traits": [], "name": "Astro", "description": "Desc", "isRecruiting": True}, conf)
    assert f == Faction(FactionSymbol.ASTRO, "X1-ABC12-ABC123", [], "Astro", "Desc", True)
