class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} #this is our hashmap

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        # we want to insert a node (key and value)
        prev = self.right.prev  
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev
   
    def remove(self, node):
        #remove the node
        prev = node.prev
        nxt = node.next
        prev.next =  nxt 
        nxt.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1    
        # find the key in map which is cache(key)

        # remove the key 
        # insert key 
        # return self.cache(key).val
        # or return -1     

    def put(self, key: int, value: int) -> None:
        #if in cache:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        # remove it from linked list and cache which is our map
        # add it to the front 
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        # insert the key 
        # #check cache if exceeds capacity remove lru and right most pointer will go to this
        # if we are removing it we have to remove it in the node list and hashmap
        
