def defenders(pawn: str) -> tuple:
    """
    Returns pawn's possible defenders
    """
    x, y = pawn[0], int(pawn[1])
    return (f'{chr(ord(x)-1)}{y-1}', f'{chr(ord(x)+1)}{y-1}')


def is_safe(pawn: str, pawns: set) -> bool:
    """
    Returns True if a pawn has at least one defender
    """
    return any([defender in pawns for defender in defenders(pawn)])


def safe_pawns(pawns: set) -> int:
    return len(list(filter(lambda x: is_safe(x, pawns), pawns)))
