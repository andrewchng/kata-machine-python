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
        
