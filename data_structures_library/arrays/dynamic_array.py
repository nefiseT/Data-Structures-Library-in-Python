"""Dynamic Array Implementation

- Automatic resizing
- Index-based access
- Append, insert, delete

Time Complexity:
- Access: O(1)
- Append: O(1) amortized
- Insert/Delete: O(n)
"""

class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0 
        self.array = [None] * capacity

    def _resize(self, new_capacity): 
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity*2)
        self.array[self.size] = value
        self.size+=1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("index out of bounds")

        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None
        self.size -= 1

        if 0 < self.size <= self.capacity // 4:
            self._resize(self.capacity // 2)

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")
        return self.array[index]

    def __str__(self):
        return str(self.array[:self.size])
    
if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.insert(1, 15)
    print(arr)
    arr.delete(2)
    print(arr)

    