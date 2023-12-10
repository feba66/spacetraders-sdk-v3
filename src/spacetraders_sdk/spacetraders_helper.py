from dacite import from_dict


def system_symbol_from_waypoint_symbol(waypoint_symbol):
    return waypoint_symbol[:waypoint_symbol.rfind("-")]
