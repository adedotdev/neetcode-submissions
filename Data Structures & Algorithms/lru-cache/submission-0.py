class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.lru = Node()
        self.mru = Node()
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def remove(self, node):
        # unlink node from list
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev  

    def insert(self, node):
        prev = self.mru.prev
        nxt = self.mru
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key):
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            left = self.lru.next
            self.remove(left)
            del self.cache[left.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)