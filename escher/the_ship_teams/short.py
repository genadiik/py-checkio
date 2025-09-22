def two_teams(sailors):
    return [
        sorted(filter(lambda n: sailors[n] > 40 or sailors[n] < 20, sailors)),
        sorted(filter(lambda n: 20 <= sailors[n] <= 40, sailors))
    ]
