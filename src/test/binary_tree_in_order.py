import unittest
from src.utils import dynamic_import, create_tree, print_tree
# from src.types import BinaryNode

class BinaryTreeInOrderTest(unittest.TestCase): 
    def test_in_order(self):
        head = create_tree()
        print("\n")
        # print(head.value)
        print_tree(head)


        


            

    
