import re
import importlib
import os
from types import ModuleType
from src.types import BinaryNode

def count_days():
    idx = 0
    def contains_day_patter(text: str):
        pattern = r'day\d+'
        if re.search(pattern, text):
            return True
        else :
            return False

    path = "./src"
    for _, dirs, _ in os.walk(path):
        for dir in dirs:
            if contains_day_patter(dir) :
                idx += 1
    return idx

def dynamic_import(kata_name: str) -> ModuleType :
    module_name = f"src.day{count_days()}.{kata_name}"
    module = importlib.import_module(module_name)
    return module


def insert_node(root, value):
    if root is None:  # Empty tree, create a new node
        return BinaryNode(value)
    elif value < root.value:  # Value is less than current node's value
        root.left = insert_node(root.left, value)  # Recursively insert left child
    else:
        root.right = insert_node(root.right, value)  # Recursively insert right child
    return root

def print_tree(root):
    if root is None:  # Base case: empty tree
        return
    print_tree(root.left)  # Recursively traverse left subtree
    print(root.value)
    print_tree(root.right)  # Recursively traverse right subtree

def create_tree():
    root = BinaryNode(5)
    root = insert_node(root, 2)  # Insert node with value 2 (left child of 5)
    root = insert_node(root, 7)  # Insert node with value 7 (right child of 5)
    root = insert_node(root, 3)  # Insert node with value 3 (left child of 2)
    root = insert_node(root, 6)  # Insert node with value 6 (right child of 2)
    root = insert_node(root, 8)  # Insert node with value 8 (right child of 7)
    return root