from typing import List
from math import degrees, acos


def checkio(a: int, b: int, c: int) -> List[int]:
    if a >= b + c or b >= a + c or c >= a + b:
        return [0, 0, 0]
    angles = []
    angles.append(int(degrees(acos((b**2 + c**2 - a**2)/(2*b*c)))+0.5))
    angles.append(int(degrees(acos((a**2 + c**2 - b**2)/(2*a*c)))+0.5))
    angles.append(int(degrees(acos((a**2 + b**2 - c**2)/(2*a*b)))+0.5))
    return sorted(angles)
