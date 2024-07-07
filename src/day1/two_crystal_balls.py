import math


def two_crystal_balls(breaks: list[bool]) -> int:
    jumpStep = math.floor(math.sqrt(len(breaks)))

    idx = 0 
    for i in range(0, len(breaks), jumpStep):
        if breaks[i]:
            idx = i - jumpStep
            break

    for j in range(idx, len(breaks)):
        if breaks[j]:
            return j

    return -1 