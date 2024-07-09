from src.types import BinaryNode

def compare_binary_trees(a : BinaryNode, b : BinaryNode) -> bool:
    if a == None and b == None:
        return True
    if a == None or b == None:
        return False
    if a.value != b.value:
        return False
    
    return compare_binary_trees(a.left, b.left) and compare_binary_trees(a.right, b.right)

