from src.types import BinaryNode

def binary_tree_bfs(root : BinaryNode, needle :int) -> bool:
    queue = [root]
    while len(queue) > 0 :
        node = queue.pop(0)
        if node is None:
            continue
        if node.value == needle:
            return True
        queue.append(node.left)
        queue.append(node.right)

    return False
