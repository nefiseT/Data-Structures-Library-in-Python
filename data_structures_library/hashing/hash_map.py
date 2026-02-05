"""
Hash Map with pluggable hash functions
"""

from hash_functions import division_hash

class HashMap:
    def __init__(self, capacity=8, hash_func = division_hash):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
        self.hash_func = hash_func
    
    def _hash(self, key):
        return self.hash_func(key, self.capacity)
    
    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
            
        bucket.append([key, value])
        self.size += 1

        if self.size / self.capacity > 0.75:
            self._resize()

    def get(self, key):
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, _ ) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False
    
    def _resize(self):

        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for k, v in bucket:
                self.put(k,v)


if __name__ == "__main__":
    # Test the HashMap

    from hash_functions import (
        division_hash,
        multiplication_hash,
        folding_hash,
        crypto_hash,
        UniversalHash
    )

    print("=== Division Hash ===")
    hm1 = HashMap(hash_func=division_hash)
    hm1.put("apple", 10)
    hm1.put("banana", 20)
    print(hm1.get("apple"))

    print("\n=== Multiplication Hash ===")
    hm2 = HashMap(hash_func=multiplication_hash)
    hm2.put("apple", 10)
    print(hm2.get("apple"))

    print("\n=== Crypto Hash ===")
    hm3 = HashMap(hash_func=crypto_hash)
    hm3.put("secure", 999)
    print(hm3.get("secure"))

    print("\n=== Universal Hash ===")
    uh = UniversalHash()
    hm4 = HashMap(hash_func=uh.hash)
    hm4.put("x", 42)
    print(hm4.get("x"))
