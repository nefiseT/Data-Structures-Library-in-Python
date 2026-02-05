"""Hash Map using Open Addressing (Linear Probing)"""

class HashMapOpenAddressing:

    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key, i):
        return (hash(key) + i ) % self.capacity
    
    def put(self, key, value):
        for i in range(self.capacity):
            idx = self._hash(key, i)
            if self.table[idx] is None or self.table[idx][0] == key:
                if self.table[idx] is None:
                    self.size += 1
                self.table[idx] = (key, value)
                return
        raise Exception("Hash table is full")
            
    def get(self, key):
        for i in range(self.capacity):
            idx = self._hash(key, i)
            if self.table[idx] is None:
                return None
            if self.table[idx][0] == key:
                return self.table[idx][1]
        return None

    def remove(self, key):
        for i in range(self.capacity):
            idx = self._hash(key, i)
            if self.table[idx] is None:
                return False
            if self.table[idx][0] == key:
                self.table[idx] = None
                self.size -= 1
                return True
        return False
    
if __name__ == "__main__":
    hm = HashMapOpenAddressing()

    hm.put("a", 1)
    hm.put("b", 2)
    hm.put("c", 3)

    print("a:", hm.get("a"))
    print("b:", hm.get("b"))

    hm.remove("a")

    print("a after removal:", hm.get("a"))
    print("b still exists:", hm.get("b"))