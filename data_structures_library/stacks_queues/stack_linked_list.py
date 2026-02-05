"""
Stack implementation using Singly Linked List

Push/Pop at head for O(1) operations

"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from linked_lists.node import SinglyNode

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self,value):
        xnode = SinglyNode(value)
        xnode.next = self.top
        self.top = xnode

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self.top.data
        self.top = self.top.next
        return value
    
    def peek (self):
        return None if self.is_empty() else self.top.data
    
    def is_empty(self):
        return self.top is None
    
if __name__ == "__main__":
    s = StackLinkedList()
    s.push(1)
    s.push(2)
    print(s.pop())
