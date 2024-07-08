import unittest
from src.utils import dynamic_import, create_tree, get_path_in_order

binary_tree_in_order = dynamic_import("binary_tree_in_order").binary_tree_in_order

class BinaryTreeInOrderTest(unittest.TestCase): 
    def test_in_order(self):
        head = create_tree()
        path = []
        get_path_in_order(head, path)
        self.assertEqual(binary_tree_in_order(head), path)
        
        


            

    
