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
        new_node = Node(value, None)
        self.length = self.length +1
        if(self.length == 0):
            self.head = new_node
            return
        new_node.prev = self.head
        self.head = new_node
    
    def pop(self) -> T: 
        if self.length == 0 :
            self.head = None
            return None
        self.length = self.length -1
        pop = self.head
        self.head = self.head.prev
        return pop.value

    def peek(self) -> T:
        if self.head:
             return self.head.value
        return None
