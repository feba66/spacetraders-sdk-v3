from collections import defaultdict
from math import sqrt
import os
from pprint import pprint
import time
from dotenv import find_dotenv, load_dotenv
from requests import Response
from spacetraders_sdk.spacetraders_enums import (
    FactionSymbol,
    WaypointTraitSymbols,
    WaypointType,
)
from spacetraders_sdk.spacetraders_objects import Meta, Waypoint
from spacetraders_sdk.spacetraders_sdk import SpaceTradersSDK
from spacetraders_sdk.spacetraders_helper import (
    sleep_till,
    system_symbol_from_waypoint_symbol,
)
import random
import string


def test_register():
    load_dotenv(find_dotenv(".env"))
    sdk = SpaceTradersSDK(os.getenv("SERVERURL"))
    userappendix = "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(7)
    )
    r = sdk.register("FEBATST" + userappendix, FactionSymbol.COSMIC)
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
    except ValueError:
        pass


def dist1(ax, ay, bx, by):
    return sqrt((ax - bx) ** 2 + (ay - by) ** 2)


def dist(a, bx, by):
    return sqrt((a[0] - bx) ** 2 + (a[1] - by) ** 2)


def dist2(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


if __name__ == "__main__":
    # test_register()
    # exit()
    load_dotenv(find_dotenv(".env"))
    sdk = SpaceTradersSDK(os.getenv("SERVERURL"))
    sdk.Login(os.getenv("TOKEN"))

    ships, m = sdk.get_ships()
    ship_coords = (ships[0].nav.route.destination.x, ships[0].nav.route.destination.y)
    system = system_symbol_from_waypoint_symbol(ships[0].nav.waypointSymbol)
    wps: list[Waypoint] = []
    page = 1
    while True:
        waypoints, m = sdk.get_waypoints(system, page)
        for w in waypoints:
            if dist(ship_coords, w.x, w.y) < ships[0].fuel.capacity / 2:
                wps.append(w)
        if m.total <= page * m.limit:
            break
        page += 1
    print(len(wps))
    # wp_list = defaultdict(list)
    for w in wps:
        traits = [t.symbol for t in w.traits]
        if WaypointTraitSymbols.MARKETPLACE in traits:
            sdk.get_market(w)
        if WaypointTraitSymbols.SHIPYARD in traits:
            sdk.get_shipyard(w)
        if WaypointTraitSymbols.PRECIOUS_METAL_DEPOSITS in traits:
            print(w)
        if WaypointTraitSymbols.RARE_METAL_DEPOSITS in traits:
            print(w)
        # if WaypointTraitSymbols.EXPLOSIVE_GASES in traits:
        #     print(w)
        if w.type == WaypointType.GAS_GIANT:
            print(w)

    goods = defaultdict(list)
    for m in sdk.markets.values():
        for i in m.imports:
            goods[i.symbol].append((m.symbol, "IMPORT"))
        for e in m.exports:
            goods[e.symbol].append((m.symbol, "EXPORT"))
        for e in m.exchange:
            goods[e.symbol].append((m.symbol, "EXCHANGE"))
    # pprint(goods)

    # siphon_place = "X1-CP67-C35"
    # sell_place = "X1-CP67-E42"
    # ship = ships[0]
    # sdk.orbit(ship)
    # try:
    #     f, n = sdk.navigate(ship, siphon_place)
    #     sleep_till(n)
    # except:
    #     pass
    # resulter(sdk.siphon(ship))
    # if w.type == WaypointType.MOON or w.type == WaypointType.ORBITAL_STATION:
    #     wp_list[w.type].append((w.x+random.randrange(-300, 300)/1000, w.y+random.randrange(-300, 300)/1000))
    # else:
    #     wp_list[w.type].append((w.x, w.y))
    # import matplotlib.pyplot as plt
    # for w in wp_list:
    #     x, y = [wp[0] for wp in wp_list[w]], [wp[1] for wp in wp_list[w]]
    #     plt.scatter(x, y, label=w)
    # plt.scatter(ships[0].nav.route.destination.x, ships[0].nav.route.destination.y, label="Ship 1")
    # plt.legend()
    # plt.show()
    # # market = sdk.get_market(ships[0].nav.waypointSymbol)
    # for m in sdk.markets.values():
    #     if m.tradeGoods:
    #         pprint(m.tradeGoods)
    # pass
    # pprint(market.tradeGoods)
