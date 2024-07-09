import unittest
from src.utils import dynamic_import, create_tree

dfs_on_binary_search_tree = dynamic_import("dfs_on_binary_search_tree").dfs_on_binary_search_tree

class BinaryTreeBFSTest(unittest.TestCase):
    def test_found_needle(self):
        root = create_tree()
        self.assertTrue(dfs_on_binary_search_tree(root, 8 ))

    def test_no_needle_found(self):
        root = create_tree()
        self.assertFalse(dfs_on_binary_search_tree(root, 1 ))

