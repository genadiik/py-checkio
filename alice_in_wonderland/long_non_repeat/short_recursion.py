def non_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    for i in range(1, len(line)):
        if line[i] in line[:i]:
            return max(line[:i], non_repeat(line[1:]), key=len)
    return line
