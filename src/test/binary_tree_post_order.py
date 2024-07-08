import unittest
from src.utils import dynamic_import, create_tree, get_path_post_order

binary_tree_post_order = dynamic_import("binary_tree_post_order").binary_tree_post_order

class BinaryTreePostOrderTest(unittest.TestCase): 
    def test_post_order(self):
        head = create_tree()
        path = []
        get_path_post_order(head, path)
        self.assertEqual(binary_tree_post_order(head), path)
        
        


            

    
