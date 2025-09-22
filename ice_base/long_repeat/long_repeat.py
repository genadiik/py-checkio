def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    longest_len = 0
    current_len = 0
    current = ''
    for c in line:
        if c == current:
            current_len += 1
        else:
            current = c
            current_len = 1
        if current_len > longest_len:
            longest_len = current_len
    return longest_len
