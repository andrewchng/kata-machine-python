from typing import List
from ..types import GraphEdge, WeightedAdjacencyList

def dfs_graph_list(graph: WeightedAdjacencyList, source: int, needle: int) -> List[int]:
    path = []
    seen = [False]* len(graph.get_edges())
    walk(graph, source, needle, seen, path)
    
    return path    
    
def walk(graph: WeightedAdjacencyList, curr: int, needle: int, seen: List[bool], path: List[int]):
    if curr == needle:
        path.append(curr)
        return True
    
    if seen[curr]:
        return False
    
    seen[curr] = True
    
    path.append(curr)
    
    edges : List[GraphEdge] = graph.get_edges()
    for edge in (edges[curr]):
        edge : GraphEdge
        if walk(graph, edge.to, needle, seen, path):
            return True
        
    path.pop()
    
    
    