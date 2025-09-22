def checkio(data):
    return data[0] if len(data) == 1 else data[0] + checkio(data[1:])
