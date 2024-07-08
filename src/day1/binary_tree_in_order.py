from src.types import BinaryNode

def binary_tree_in_order(head: BinaryNode) -> list[int]:
    path = []
    walk(head, path)
    return path

def walk(curr : BinaryNode, path: list[int]):
    if curr is None :
        return
    walk(curr.left, path)
    path.append(curr.value)
    walk(curr.right, path)