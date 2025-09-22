import re


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    return max([len(i[0]) for i in re.finditer(r"(\w)\1*", line)]) if line else 0
