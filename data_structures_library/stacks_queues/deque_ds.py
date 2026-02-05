"""
double ended queue

Deque implementation using Doubly Linked List

"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from linked_lists.node import DoublyNode

class Deque:
    def __init__(self):
        self.front = None 
        self.rear = None

    def add_front(self, value):
        node = DoublyNode(value)
        if not self.front:
            self.front = self.rear = node 
            return
        node.next = self.front
        self.front.prev = node 
        self.front = node

    def add_rear(self, value):
        node = DoublyNode(value)
        if not self.rear:
            self.front = self.rear = node
            return
        
        self.rear.next = node
        node.prev = self.rear
        self.rear = node

    def remove_front(self):
        if not self.front:
            raise IndexError("deque is empty")
        value = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None 
        else: 
            self.rear = None 
        return value
    
    def remove_rear(self):
        if not self.rear:
            raise IndexError("deque is empty")
        value = self.rear.data
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        else:
            self.front = None

        return value

    def to_list(self):
        result = []
        current = self.front
        while current:
            result.append(current.data)
            current = current.next
        return result
    
if __name__ == "__main__":
    dq = Deque()
    dq.add_front(20)
    dq.add_front(50)
    dq.add_front(33)
    print(f"Before: {dq.to_list()}")
    removed = dq.remove_rear()
    print(f"After: {dq.to_list()}")
    print(f"removed: {removed}")


## dq creates a new Deque object, so we can abbply methods
