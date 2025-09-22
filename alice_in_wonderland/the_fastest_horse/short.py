def fastest_horse(races: list) -> int:
    races = list(map(lambda r: r.index(min(r)), races))
    return sorted(races, key=races.count)[-1] + 1
