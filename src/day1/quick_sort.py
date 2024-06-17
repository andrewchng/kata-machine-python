def quick_sort(arr: list[int]):
    qs(arr, 0, len(arr) - 1)

def qs(arr: list[int], lo: int, hi:int):
    if lo >= hi:
        return
    
    # initial sort first before we sort the children
    pivot = partition(arr, lo, hi)

    qs(arr, lo, pivot - 1)
    qs(arr, pivot + 1, hi)

def partition(arr: list[int], lo: int, hi: int) -> int:
    pivot = arr[hi]
    idx = lo - 1

    # remember to use hi as the condition as we don't need to include hi, need to start from lo too
    for i in range(lo, hi):
        if arr[i] <= pivot:
            idx += 1
            arr[idx], arr[i] = arr[i], arr[idx]

    # pivot will point to last swapped index, need ++ to pinpoint the position in which the pivot will swap with
    idx +=1
    arr[idx], arr[hi] = arr[hi], arr[idx]

    return idx  