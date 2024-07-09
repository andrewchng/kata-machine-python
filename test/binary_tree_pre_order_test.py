import unittest
from src.utils import dynamic_import, create_tree, get_path_pre_order

binary_tree_pre_order = dynamic_import("binary_tree_pre_order").binary_tree_pre_order

class BinaryTreePostOrderTest(unittest.TestCase): 
    def test_pre_order(self):
        head = create_tree()
        path = []
        get_path_pre_order(head, path)
        self.assertEqual(binary_tree_pre_order(head), path)
        
        


            

    
