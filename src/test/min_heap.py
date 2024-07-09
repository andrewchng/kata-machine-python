import unittest
from src.types import BinaryNode
from src.utils import create_tree, dynamic_import, insert_node_left, print_binary_tree

min_heap = dynamic_import("min_heap").min_heap

class MinHeapTest(unittest.TestCase):
    def test_min_heap(self):
        heap = min_heap() 
        heap.insert(5)
        heap.insert(3)
        heap.insert(69)
        heap.insert(420)
        heap.insert(4)
        heap.insert(1)
        heap.insert(8)
        heap.insert(7)
        self.assertEqual(heap.length).toEqual(8)
        self.assertEqual(heap.delete()).toEqual(1)
        self.assertEqual(heap.delete()).toEqual(3)
        self.assertEqual(heap.delete()).toEqual(4)
        self.assertEqual(heap.delete()).toEqual(5)
        self.assertEqual(heap.length).toEqual(4)
        self.assertEqual(heap.delete()).toEqual(7)
        self.assertEqual(heap.delete()).toEqual(8)
        self.assertEqual(heap.delete()).toEqual(69)
        self.assertEqual(heap.delete()).toEqual(420)
        self.assertEqual(heap.length).toEqual(0)

         