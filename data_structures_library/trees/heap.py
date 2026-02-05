""" min max  w seperated class structure for each """

"""Operation,Complexity
Heapify (Building the heap),O(N)
Push (Inserting an element),O(logN)
Pop (Removing the root),O(logN)
Peek (Looking at the root),O(1)
"""

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self,value):
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1)

    def pop(self):
        if not self.heap :
            return None
        self._swap(0, len(self.heap) -1)
        val = self.heap.pop()
        self._heapify_down(0)
        return val
    
    def _heapify_up(self,idx):
        parent = (idx -1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self._swap(idx, parent)
            self._heapify_up(parent)

    def _heapify_down (self,idx):
        smallest = idx
        l = 2 * idx + 1
        r = 2 * idx + 2

        if l < len(self.heap) and self.heap[1] < self.heap[smallest]:
            smallest = 1
        if r < len(self.heap) and self.heap[1] < self.heap[smallest]:
            smallest = r

        if smallest != idx:
            self._swap(idx, smallest)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]



class MaxHeap:
    def __init__(self):
        self.heap = []

    def push (self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) -1)

    def pop(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) -1)
        val = self.heap.pop()
        self._heapify_down(0)
        return val
    
    def _heapify_up(self, idx):
        parent = (idx - 1) //2
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self._swap(idx, parent)
            self._heapify_up(parent)

    def _heapify_down (self,idx):
        largest = idx 
        l = 2 * idx + 1
        r = 2 * idx + 2


        if l < len(self.heap) and self.heap[1] > self.heap[largest]:
            largest = 1
        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != idx:
            self._swap(idx, largest)
            self._heapify_down(largest)

    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


if __name__ == "__main__":
    print("Min Heap:")
    min_heap = MinHeap()
    for v in [5, 3, 8, 1]:
        min_heap.push(v)
    while min_heap.heap:
        print(min_heap.pop(), end=" ")

    print("\n\nMax Heap:")
    max_heap = MaxHeap()
    for v in [5, 3, 8, 1]:
        max_heap.push(v)
    while max_heap.heap:
        print(max_heap.pop(), end=" ")

