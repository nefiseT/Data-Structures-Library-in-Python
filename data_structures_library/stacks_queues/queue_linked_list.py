"""
Queue implementation using Linked List

O(1) enqueue and dequeue
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from linked_lists.node import SinglyNode


class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = SinglyNode(value)
        if not self.rear:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return value

    def is_empty(self):
        return self.front is None


if __name__ == "__main__":
    q = QueueLinkedList()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    print(q.dequeue())
