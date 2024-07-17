class Node :
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class singly_linked_list():

    def __init__(self, length = 0):
        self.length = length
        self.head = None
        self.tail = None

    def prepend(self, item : int):
        node = Node(item)
        if self.length == 0:
            self.length += 1
            self.head = self.tail = node
            return  
    
        self.length += 1
        node.next = self.head
        self.head = node 
    
    def insert_at(item: int, idx: int ):
        return
    
    def append(self, item: int):
        node = Node(item)
        if self.length == 0 :
            self.head = self.tail = node
            self.length += 1
            return
        self.length += 1
        self.tail.next = node
        self.tail = node
    
    def remove(self, item: int) -> int:
        if self.length == 0:
            return None
        if self.length == 1 and self.head.value == item:
            self.head = self.tail
            self.length -= 1
            return
        
        curr = self.head
        if (curr.value == item):
            self.length -=1
            self.head = curr.next
            return curr.value
        for _ in range(self.length-1):
            prev = curr
            curr =  curr.next
            if curr.value == item:
                self.length -= 1
                prev.next = curr.next
                return curr.value
        return None
    
    def get(self, idx: int) -> int:
        if idx == 0:
            return self.head.value
        if idx == self.length - 1:
            return self.tail.value
        
        curr = self.head
        for _ in range(idx):
            curr = curr.next
        return curr.value
    
    def remove_at(self, idx : int) -> int:
        if self.length == 0 : 
            return None
        if idx == 0:
            if self.length == 1:
                self.length -= 1
                v = self.head.value
                self.head = self.tail = None
                return v
            self.length -= 1
            v = self.head.value
            self.head = self.head.next
            return v
        
        curr = self.head
        prev = None
        for _ in range(idx):
            prev = curr
            curr =  curr.next
        
        v = curr.value
        prev.next = curr.next
        self.length -= 1

        if self.length == 1:
            self.head = self.tail

        return v