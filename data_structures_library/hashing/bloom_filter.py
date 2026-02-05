"""bloom filter implementation"""

import hashlib

class BloomFilter:
    def __init__(self, size=100, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        for i in range(self.hash_count):
            digest = hashlib.md5(f"{item}{i}".encode()).hexdigest()
            yield int(digest, 16) % self.size

    def add(self, item):
        for idx in self._hashes(item):
            self.bit_array[idx] = 1

    def contains(self, item):
        return all(self.bit_array[idx] == 1 for idx in self._hashes(item))

if __name__ == "__main__":
    bf = BloomFilter(size=50, hash_count=3)

    bf.add("apple")
    bf.add("banana")

    print("apple:", bf.contains("apple"))
    print("banana:", bf.contains("banana"))
    print("cherry:", bf.contains("cherry"))
