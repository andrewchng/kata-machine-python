from typing import List
import unittest
from src.types import WeightedAdjacencyList, GraphEdge
# from ..src.day1 import dfs_graph_list
from src.utils import dynamic_import

dfs_graph_list = dynamic_import("dfs_graph_list").dfs_graph_list

class DFSGraphList(unittest.TestCase):
    def test_dfs(self):
        graph_list: WeightedAdjacencyList = WeightedAdjacencyList()
        
        edges0 : List[GraphEdge] = [
            GraphEdge(to=1,weight=3),
            GraphEdge(to=2,weight=1)
        ]
        graph_list.add_edges(edges0)
        
        edges1 : List[GraphEdge] = [
            GraphEdge(to=4,weight=1),
        ]
        graph_list.add_edges(edges1)
   
        edges2 : List[GraphEdge] = [
            GraphEdge(to=3,weight=7),
        ]
        graph_list.add_edges(edges2)
        
        graph_list.add_edges([])
        
        edges4 : List[GraphEdge] = [
            GraphEdge(to=1,weight=1),
            GraphEdge(to=3,weight=5),
            GraphEdge(to=5,weight=2)
        ]
        graph_list.add_edges(edges4)
        
        edges5 : List[GraphEdge] = [
            GraphEdge(to=1,weight=18),
            GraphEdge(to=6,weight=1)
        ]
        graph_list.add_edges(edges5)
        
        edges6 : List[GraphEdge] = [
            GraphEdge(to=3,weight=1),
        ]
        graph_list.add_edges(edges6)
        
    
        self.assertEqual(dfs_graph_list(graph_list, 0 ,6), [0 , 1, 4, 5, 6] )