class Node():
    def __init__(self, value, next = None, prev = None) -> None:
        self.value : int  = value
        self.next : Node = next
        self.prev : Node = prev

class least_recently_used():
    def __init__(self, capacity) -> None:
        self.head : Node = None
        self.tail : Node = None
        self.capacity : int = capacity
        self.length : int = 0
        self.lookup : dict[str, Node]= {}
        self.reverse_lookup : dict[Node, str] = {}
        pass
    
    def update(self, key : str, value : int) -> None:
        node = self.lookup.get(key)
        if node is None:
            new_node = Node(value)
            self.prepend(new_node)
            self.length += 1
            self.lookup[key] = new_node
            self.reverse_lookup[new_node] = key
            self.trim_cache()
        else:
            node.value = value
            self.detach(node)
            self.prepend(node)
    
    def get(self, key : str) -> int:
        node = self.lookup.get(key)
        if node is None:
            return None
        
        self.detach(node)
        self.prepend(node)
        return node.value
    
    def detach(self, node : Node):
        if self.head is node:
            self.head = node.next
            
        if self.tail is node:
            self.tail = node.prev
        
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
            
    def prepend(self, node : Node):
        if self.head is None:
            self.tail = self.head = node
            return
           
        node.next = self.head
        self.head.prev = node
        self.head = node
    
    def trim_cache(self):
        if self.length <= self.capacity:
            return
        
        tail = self.tail
        self.detach(tail)
        key = self.reverse_lookup.get(tail)
        self.lookup.pop(key)
        self.reverse_lookup.pop(tail)
        self.length -= 1