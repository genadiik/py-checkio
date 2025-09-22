def checkio(data: str) -> bool:
    any_digit = any([c.isdigit() for c in data])
    any_upper = any([c.isupper() for c in data])
    any_lower = any([c.islower() for c in data])
    return len(data) >= 10 and any_digit and any_upper and any_lower
