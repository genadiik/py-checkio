def flat_list(array):
    if any(map(lambda x: isinstance(x, list), array)):
        result = []
        for i in array:
            result.extend(i) if isinstance(i, list) else result.append(i)
        return flat_list(result)
    return array
