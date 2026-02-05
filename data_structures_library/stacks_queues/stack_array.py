"""
Stack implementation using Dynamic Array

LIFO: Last In First Out

"""

class StackArray:
    def __init__(self): 
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
if __name__=="__main__":
    s = StackArray()
    s.push(10)
    s.push(30)
    print(s.pop())
    print(s.peek())