from src.types import BinaryNode

def dfs_on_binary_search_tree(head : BinaryNode, needle: int ) -> bool:
    return search(head, needle)


def search(curr : BinaryNode, needle: int):
    if curr is None:
        return False
    if curr.value == needle:
        return True
    
    if curr.value < needle:
        return search(curr.right, needle)
    else:
        return search(curr.left, needle)
    