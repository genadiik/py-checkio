def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0:
        return 0
    return sum(array[0::2]) * array[-1]
