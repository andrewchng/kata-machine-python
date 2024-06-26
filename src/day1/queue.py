class Node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.length +=1
            self.head = self.tail = new_node
            return
        self.length +=1
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.length ==0 :
            return None
        self.length -=1
        dequeued = self.head
        self.head = self.head.next
        return dequeued.value
    
    def peek(self):
        if self.head != None:
            return self.head.value
        return None