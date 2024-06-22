import datetime
import time
from spacetraders_sdk.spacetraders_constants import TIME_FORMAT
from spacetraders_sdk.spacetraders_objects import Cooldown, ShipNav


def system_symbol_from_waypoint_symbol(waypoint_symbol):
    return waypoint_symbol[: waypoint_symbol.rfind("-")]


def parse_time(tstr: str):
    return datetime.strptime(tstr, TIME_FORMAT)


def get_time_diff(big: datetime, small: datetime):
    return (big - small).total_seconds()


def time_till(future: str):
    return get_time_diff(parse_time(future), datetime.utcnow())


def sleep_till(nav: ShipNav = None, cooldown: Cooldown = None):
    if nav is not None:
        t = max(0, time_till(nav.route.arrival))
    elif cooldown is not None:
        t = max(0, time_till(cooldown.expiration))
    else:
        return
    print(f"Sleep for {t}")
    time.sleep(t)
