from pathlib import Path
import os, re
from src.utils import count_days

signature_map = {
    "linear_search" : "def linear_search(haystack:list[int], needle:int) -> bool:",
    "binary_search" : "def binary_search(haystack:list[int], needle:int) -> bool:",
    "quick_sort" : "def quick_sort(arr: list[int]) :",
    "bubble_sort": "def bubble_sort(arr: list[int]):",
    "two_crystal_balls" : "def two_crystal_balls(breaks: list[bool]) -> int:",
    "maze_solver" : """from typing import List, Tuple\n\nPoint = Tuple[int, int]\ndef maze_solver(maze: List[str], wall: str, start:Point, end: Point) -> List[Point]:""",
    "stack" : """
from typing import Generic, TypeVar

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T, prev:"Node[T]"= None):
        self.value = value
        self.prev = prev    

class Stack :
    def __init__(self, length : int = 0, head : "Node[T]" = None):
        self.length = length
        self.head = head

    def push(self, value: T) :
        return
  
    def pop(self) -> T: 
        return

    def peek(self) -> T:
        return
        """,
    "queue":"""class Node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        return
    
    def dequeue(self):
        return
    
    def peek(self):
        return
        """,
    "binary_tree_in_order" : """
from src.types import BinaryNode

def binary_tree_in_order(head: BinaryNode) -> list[int]:

    """,
    "binary_tree_post_order" : """
from src.types import BinaryNode

def binary_tree_post_order(head: BinaryNode) -> list[int]:
""",
"binary_tree_pre_order" : """
from src.types import BinaryNode

def binary_tree_pre_order(head: BinaryNode) -> list[int]:    
""",
"compare_binary_trees" : """from src.types import BinaryNode

def compare_binary_trees(a : BinaryNode, b : BinaryNode) -> bool:
""",

"binary_tree_bfs" : """from src.types import BinaryNode

def binary_tree_bfs(root : BinaryNode, needle :int) -> bool:""",
"dfs_on_binary_search_tree": """
from src.types import BinaryNode

def dfs_on_binary_search_tree(head : BinaryNode, needle: str ) -> bool:"""
}

def generate_new_kata():
    days = count_days()
    folder_name = f"day{days+1}"
    src_dir = Path("src")/folder_name
    src_dir.mkdir(exist_ok=True)

    for kata_name, signature in signature_map.items():
        kata_file = src_dir / f"{kata_name}.py"
        with kata_file.open("w") as f:
            f.write(f"{signature}")
    init_file = src_dir / "__init__.py"
    with init_file.open("w") as f:
        f.write(f"# this is the __init__.py file for {folder_name}")
    

if __name__ == '__main__':
    generate_new_kata()

