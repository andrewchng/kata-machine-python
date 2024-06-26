from pathlib import Path
import os, re
from src.utils import count_days

signature_map = {
    "linear_search" : "def linear_search(haystack:list[int], needle:int) -> bool:",
    "binary_search" : "def binary_search(haystack:list[int], needle:int) -> bool:",
    "quick_sort" : "def quick_sort(arr: list[int]) :",
    "maze_solver" : """from typing import List, Tuple\n\nPoint = Tuple[int, int]\ndef maze_solver(maze: List[str], wall: str, start:Point, end: Point) -> List[Point]:""",
    "stack" : """
from typing import Generic, TypeVar

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T, prev:"Node[T]"):
        self.value = value
        self.prev = prev    

class Stack :
    def __init__(self, length, head):
        self.length = length
        self.head = head

    def push(value) :
        return
  
    def pop() -> "Node[T]": 
        return

    def peek() -> "Node[T]":
        return
        """
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

