import unittest
from src.utils import dynamic_import
from src.types import WeightedAdjacencyMatrix

bfs_graph_matrix = dynamic_import("bfs_graph_matrix").bfs_graph_matrix

class BFSGraphMatrix(unittest.TestCase):
    def test_graph_matrix(self):
        ans = [
            0,
            1,
            4,
            5,
            6,
        ]
        graph = WeightedAdjacencyMatrix()
            #    0  1  2   3  4  5  6
        row_0 = [0, 3, 1,  0, 0, 0, 0]  # 0
        row_1 = [0, 0, 0,  0, 1, 0, 0]  # 1
        row_2 = [0, 0, 7,  0, 0, 0, 0]  # 2
        row_3 = [0, 0, 0,  0, 0, 0, 0]  # 3
        row_4 = [0, 1, 0,  5, 0, 2, 0]  # 4
        row_5 = [0, 0, 18, 0, 0, 0, 1]  # 5
        row_6 = [0, 0, 0,  1, 0, 0, 1]  # 6

        graph.add_matrix_row(row_0)
        graph.add_matrix_row(row_1)
        graph.add_matrix_row(row_2)
        graph.add_matrix_row(row_3)
        graph.add_matrix_row(row_4)
        graph.add_matrix_row(row_5)
        graph.add_matrix_row(row_6)
                    
        self.assertEqual(bfs_graph_matrix(graph, 0, 6), ans)
        self.assertEqual(bfs_graph_matrix(graph, 6, 0), [])
    
            
        
        