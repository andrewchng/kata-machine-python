def linear_search(haystack:list, needle:int) -> int:
    for item in haystack:
        if item == needle:
            return needle
    return -1
    

