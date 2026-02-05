"""
Static Array Implementation

- Fixed size
- No resizing
"""

class StaticArray:
    def __init__(self, size):
        self.size = size 
        self.array = [None] * size

    def set(self, index, value):
        if 0<= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("index out of bounds")
        
    def ge(self,index):
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("ındex out of bounds")
    
    def __str__(self):
        return str(self.array)
    

if __name__ == "__main__":
    arr = StaticArray(5)
    arr.set(0, 10)
    arr.set(1, 20)
    print(arr)
    
