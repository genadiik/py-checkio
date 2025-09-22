from typing import List


def is_winner(party: str, game_result: List[str]):
    """
    Checks if party ('X' or 'O') is a winner
    """

    # Board scheme:
    # (0,0) (0,1) (0,2)
    # (1,0) (1,1) (1,2)
    # (2,0) (2,1) (2,2)
    win_rows = (
        ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2))
    )

    for row in win_rows:
        if all([game_result[x][y] == party for x, y in row]):
            return True
    return False


def checkio(game_result: List[str]) -> str:
    if is_winner('X', game_result):
        return 'X'
    if is_winner('O', game_result):
        return 'O'
    return 'D'
