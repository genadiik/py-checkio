def group_equal(data):
    if not data:
        return []
    result = [[data[0]]]
    for i in data[1:]:
        if i == result[-1][0]:
            result[-1].append(i)
        else:
            result.append([i])
    return result
