from typing import List

class BinaryNode():
    def __init__(self, value = None, left = None, right = None):
        self.right = right
        self.left = left
        self.value = value

class GraphEdge:
    def __init__(self, to: int, weight: float):
        self.to = to
        self.weight = weight
        
class WeightedAdjacencyList:
    def __init__(self):
        self.graph_edges: List[List[GraphEdge]] = []

    def add_edges(self, edges: List[GraphEdge]):
        self.graph_edges.append(edges)

    def get_edges(self) -> List[List[GraphEdge]]:
        return self.graph_edges

class WeightedAdjacencyMatrix:
    def __init__(self) -> None:
        self.matrix : List[List[int]] = []
    
    def add_matrix_row(self, matrix_row:List[int]):
        self.matrix.append(matrix_row)
        
    def get_matrix(self):
        return self.matrix
    
    
