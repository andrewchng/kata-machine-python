import unittest
from src.types import BinaryNode
from src.utils import dynamic_import, create_tree, insert_node, insert_node_left

compare_binary_trees = dynamic_import("compare_binary_trees").compare_binary_trees

class TestCompareBinaryTrees(unittest.TestCase):
    def test_same_binary_trees(self):
        a = create_tree()
        self.assertTrue(compare_binary_trees(a, a))

    def test_different_binary_trees_value(self):
        a = create_tree()
        b = BinaryNode(5)
        insert_node(b, 2)
        insert_node(b, 7)
        insert_node(b, 3)
        insert_node(b, 6)
        insert_node(b, 9)
        self.assertFalse(compare_binary_trees(a, b))

    def test_different_binary_trees_none(self):
        a = create_tree()
        self.assertFalse(compare_binary_trees(a, None))

    def test_different_binary_trees_structure(self):
        a = create_tree()
        b = BinaryNode(5)
        insert_node(b, 2)
        insert_node(b, 7)
        insert_node_left(b, 3)
        insert_node(b, 6)
        insert_node(b, 9)
        self.assertFalse(compare_binary_trees(a, None))

