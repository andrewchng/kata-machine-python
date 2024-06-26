from typing import Generic, TypeVar

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T, prev:"Node[T]"= None):
        self.value = value
        self.prev = prev    

class Stack :
    def __init__(self, length : int= None, head : "Node[T]" = None):
        self.length = length
        self.head = head

    def push(self, value: T) :
        return
  
    def pop(self) -> "Node[T]": 
        return

    def peek(self) -> "Node[T]":
        return
        
