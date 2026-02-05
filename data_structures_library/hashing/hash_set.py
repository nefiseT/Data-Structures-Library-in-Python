from hashing.hash_map import HashMap 

class HashSet:
    def __init__(self, hash_func=None):
        self.map = HashMap(hash_func = hash_func)

        def add(self, key):
            self.map.put(key, True)

        def contains(self, key):
            return self.map.get(key) is not None 
        
        def remove(self, key):
            return self.map.remove(key)