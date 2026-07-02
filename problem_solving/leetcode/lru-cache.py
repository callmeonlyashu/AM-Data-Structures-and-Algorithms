"""Link: https://leetcode.com/problems/lru-cache/"""

# Using Ordered Dict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.lru_cache:
            self.lru_cache.move_to_end(key, last=True)
            return self.lru_cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru_cache:
            self.lru_cache[key] = value
            self.lru_cache.move_to_end(key, last=True)
        else:
            self.lru_cache[key] = value
        
        if len(self.lru_cache) > self.capacity:
            self.lru_cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
