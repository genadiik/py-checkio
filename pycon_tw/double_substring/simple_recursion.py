def double_substring(line):
    if len(line) <= 1:
        return 0

    for i in range(len(line)//2 + 1):
        if line[:i] in line[i:]:
            result = i

    return max(result, double_substring(line[1:]))
