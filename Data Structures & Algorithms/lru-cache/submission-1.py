class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.cap = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head        

    def _rm(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add(self, node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._rm(node)
        self._add(node)
        return node.val        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._rm(self.map[key])
        node = Node(key, value)
        self.map[key] = node
        self._add(node)
        if len(self.map) > self.cap:
            lsu = self.tail.prev
            self._rm(lsu)
            del self.map[lsu.key]
