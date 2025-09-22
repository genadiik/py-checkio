import itertools as it

def count_consecutive_summers(num):
    return sum([1 for i in range(1, num+1) if any(filter(num.__eq__, it.accumulate(range(i, num+1))))])
