def checkio(text: str) -> str:
    return sorted(list('abcdefghijklmnopqrstuvwxyz'), key=text.lower().count, reverse=True)[0]
