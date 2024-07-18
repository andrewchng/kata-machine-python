from typing import List
from src.types import WeightedAdjacencyList

def dijkstra_list(source : int, sink : int, arr: WeightedAdjacencyList) -> List[int]:
    
    infinity = 99999999
    seen : List[bool] = [False] * len(arr.get_edges())
    prev : List[int] = [-1] * len(arr.get_edges())    
    dists : List[int] = [infinity] * len(arr.get_edges())
    
    dists[source] = 0
    while has_unvisited(seen, dists, infinity):
        lo = get_lowest_unvisited(seen, dists, infinity)
        seen[lo] = True
        
        adj = arr.get_edges()[lo]
        
        for edge in adj:
            if seen[edge.to] :
                continue
            dist = dists[lo] + edge.weight
            if dist < dists[edge.to]:
                prev[edge.to] = lo
                dists[edge.to] = dist
    
    
    curr = sink
    out: List[int] = []
    
    while prev[curr] != -1:
        out.append(curr)
        curr = prev[curr]
        
    out.append(source)
    return out[::-1]

def has_unvisited(seen : List[bool], dists: List[int], infinity):
    has_unvisited = False
    for i in range(len(seen)):
        if not seen[i] and dists[i] < infinity:
            has_unvisited = True
            break
    return has_unvisited

def get_lowest_unvisited(seen : List[bool], dists: List[int], infinity):
    idx = -1
    lowest_distance = infinity
    
    for i in range(len(seen)):
        if seen[i]:
            continue
        if lowest_distance > dists[i]:
            lowest_distance = dists[i]
            idx = i
        
    return idx