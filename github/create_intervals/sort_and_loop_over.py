def create_intervals(data):
    """
        Creates a list of intervals out of set of ints.
    """
    if len(data) == 0:
        return []
    data = sorted(list(data))
    intervals = []
    start = end = data[0]

    for i in range(1, len(data)):
        if data[i-1] + 1 == data[i]:
            end = data[i]
        else:
            intervals.append((start, end))
            start = end = data[i]

    intervals.append((start, end))

    return intervals
