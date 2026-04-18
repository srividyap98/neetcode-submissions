class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

        # find the key in map which is cache(key)
        # remove the key 
        # insert key 
        # return self.cache(key).val
        # or return -1     

    def put(self, key: int, value: int) -> None:
        #if in cache:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        # remove it from linked list and cache which is our map
        # add it to the front 
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
        # insert the key 
        # #check cache if exceeds capacity remove lru and right most pointer will go to this
        # if we are removing it we have to remove it in the node list and hashmap
        
