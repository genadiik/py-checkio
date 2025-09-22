import re

def checkio(data: str) -> bool:
    return len(data) >= 10 and re.match(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])', data) != None
