from typing import List

def checkio(data: List[int]) -> [int, float]:
    s = sorted(data)
    return (s[len(s)//2] + s[len(s)//2+len(s)%2-1]) / 2
