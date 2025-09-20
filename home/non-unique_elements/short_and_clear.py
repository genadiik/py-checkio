def checkio(data: list) -> list:
    return [num for num in data if data.count(num) > 1]
