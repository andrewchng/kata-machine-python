from typing import List
import unittest
from src.utils import dynamic_import
from src.types import GraphEdge, WeightedAdjacencyList

dijkstra_list = dynamic_import("dijkstra_list").dijkstra_list

class DijkstraList(unittest.TestCase):
    def test_dijkstra_list(self):
        ans = [0, 1, 4, 5, 6]
        graph_list = WeightedAdjacencyList()
        edges0 : List[GraphEdge] = [
            GraphEdge(to=1,weight=3),
            GraphEdge(to=2,weight=1)
        ]
        graph_list.add_edges(edges0)
        
        edges1 : List[GraphEdge] = [
            GraphEdge(to=0,weight=3),
            GraphEdge(to=2,weight=4),
            GraphEdge(to=4,weight=1),
        ]
        graph_list.add_edges(edges1)
   
        edges2 : List[GraphEdge] = [
            GraphEdge(to=1,weight=4),
            GraphEdge(to=3,weight=7),
            GraphEdge(to=0,weight=1),
        ]
        graph_list.add_edges(edges2)
        
        edges3 : List[GraphEdge] = [
            GraphEdge(to=2,weight=7),
            GraphEdge(to=4,weight=5),
            GraphEdge(to=6,weight=1),
        ]
        graph_list.add_edges(edges3)
        
        edges4 : List[GraphEdge] = [
            GraphEdge(to=1,weight=1),
            GraphEdge(to=3,weight=5),
            GraphEdge(to=5,weight=2)
        ]
        graph_list.add_edges(edges4)
        
        edges5 : List[GraphEdge] = [
            GraphEdge(to=6,weight=1),
            GraphEdge(to=4,weight=2),
            GraphEdge(to=2,weight=18)
        ]
        graph_list.add_edges(edges5)
        
        edges6 : List[GraphEdge] = [
            GraphEdge(to=3,weight=1),
            GraphEdge(to=5,weight=1),
        ]
        graph_list.add_edges(edges6)
        
        
        self.assertEqual(dijkstra_list(0, 6, list), ans)
        