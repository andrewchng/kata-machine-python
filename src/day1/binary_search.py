import math

def binary_search(haystack:list, needle:int) -> bool:
    lo = 0
    hi = len(haystack)
    while lo < hi:
        mid = math.floor(lo + ( hi - lo ) / 2)
        if needle == haystack[mid]:
            return True
        elif needle < haystack[mid]:
            hi = mid
        else:
            lo = mid + 1
    return False

#[lo, hi)