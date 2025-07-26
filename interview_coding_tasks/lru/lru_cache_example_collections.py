from collections import OrderedDict

class LRUCache:
    """
    LRU (Least Recently Used) cache
    with O(1) time complexity for both get and put operations
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Move this key to the end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        # If key exists, update and move to end
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        
        # If at capacity, remove least recently used item (first item)
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        
        # Add new item
        self.cache[key] = value
