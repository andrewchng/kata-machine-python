from typing import List
from ..types import WeightedAdjacencyMatrix

def bfs_graph_matrix(graph: WeightedAdjacencyMatrix, source: int, needle : int) -> List[int]:
    seen = [False] * len(graph.get_matrix())
    prev = [-1] * len(graph.get_matrix())
    
    seen[source] = True
    q = [source]
        
    while len(q):
        curr : int = q.pop(0)

        if curr == needle:
            break
        
        matrix_row : List[int] = graph.get_matrix()[curr]
        for i in range(len(matrix_row)):
            if seen[i]:
                continue
            if matrix_row[i] == 0 :
                continue
            prev[i] = curr
            seen[i] = True
            q.append(i)
            
    # rebuild path

    if prev[needle] == -1:
        return []       
    
    curr = needle
    out = []
    while prev[curr] != -1:
       out.append(curr)
       curr = prev[curr]

    return [source] + out[::-1] 