""" same as heap file but w baseheap class w composition """

class Heap:
    def __init__(self, comparator = None):
        self.heap = []
        self.is_less_than = comparator if comparator else lambda a, b: a< b 

    def _swap(self, i, j ):
        self.heap[i] , self.heap[j] = self.heap[j] , self.heap[i]

    def push(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) -1 )
        val = self.heap.pop()
        self._heapify_down(0)
        return val
        
    def _heapify_up (self, idx):
        parent = (idx -1 )//2
# abstract comparator
        if idx > 0 and self.is_less_than(self.heap[idx], self.heap[parent]):
            self._swap(idx, parent)
            self._heapify_up(parent)

    def _heapify_down(self,idx):
        switchNode = idx        #will be used for both largest and smallest
        l = 2 * idx + 1
        r = 2 * idx + 2

        if l < len(self.heap) and self.is_less_than(self.heap[l], self.heap[switchNode]):
            switchNode = l
        if r < len(self.heap) and self.is_less_than(self.heap[r], self.heap[switchNode]):
            switchNode = r

        if switchNode != idx:
            self._swap(idx, switchNode)
            self._heapify_down(switchNode)

min_heap = Heap()   #default
max_heap = Heap(comparator=lambda a, b: a>b)    #custom logic

if __name__ == '__main__':
    # Example usage for min-heap
    print("Min-Heap Operations:")
    min_heap.push(10)
    min_heap.push(5)
    min_heap.push(20)
    min_heap.push(1)
    print("Heap after pushes:", min_heap.heap)
    print("Popped:", min_heap.pop())
    print("Heap after pop:", min_heap.heap)
    print("Popped:", min_heap.pop())
    print("Heap after pop:", min_heap.heap)

    print("\nMax-Heap Operations:")
    max_heap.push(10)
    max_heap.push(5)
    max_heap.push(20)
    max_heap.push(1)
    print("Heap after pushes:", max_heap.heap)
    print("Popped:", max_heap.pop())
    print("Heap after pop:", max_heap.heap)
    print("Popped:", max_heap.pop())
    print("Heap after pop:", max_heap.heap)
