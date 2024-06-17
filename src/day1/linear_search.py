def linear_search(haystack:list, needle:int) -> bool:
    for item in haystack:
        if item == needle:
            return True
    return False