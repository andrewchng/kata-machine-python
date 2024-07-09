import unittest
from src.utils import dynamic_import, create_tree

binary_tree_bfs = dynamic_import("binary_tree_bfs").binary_tree_bfs

class BinaryTreeBFSTest(unittest.TestCase):
    def test_found_needle(self):
        root = create_tree()
        self.assertTrue(binary_tree_bfs(root, 8 ))

    def test_no_needle_found(self):
        root = create_tree()
        self.assertFalse(binary_tree_bfs(root, 1 ))

