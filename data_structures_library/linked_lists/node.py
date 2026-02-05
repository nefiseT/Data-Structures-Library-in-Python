"""
node definition for linked lists
"""

class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None