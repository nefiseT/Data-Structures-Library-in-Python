"""
Circular Singly Linked List
"""

from node import SinglyNode


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = SinglyNode(data)

        if not self.head:
            self.head = node
            node.next = node
            return

        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        curr.next = node
        node.next = self.head

    def delete(self, key):
        if not self.head:
            return False

        curr = self.head
        prev = None

        while True:
            if curr.data == key:
                if prev:
                    prev.next = curr.next
                else:
                    # deleting head
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    self.head = curr.next
                    tail.next = self.head
                return True

            prev = curr
            curr = curr.next
            if curr == self.head:
                break

        return False
    
    def search(self, key):
        if not self.head:
            return False

        curr = self.head
        while True:
            if curr.data == key:
                return True
            curr = curr.next
            if curr == self.head:
                break
        return False

    def traverse(self):
        result = []
        if not self.head:
            return result

        curr = self.head
        while True:
            result.append(curr.data)
            curr = curr.next
            if curr == self.head:
                break
        return result
if __name__ == "__main__":
    dll = CircularLinkedList()

    dll.insert(3)
    dll.insert(2)
    dll.insert(1)

    print("Forwrd:", dll.traverse())
    print("Backward:", dll.traverse())

    dll.delete(2)

    print("----After deletint 2----")
    print("Forward:", dll.traverse())
    print("Backward:", dll.traverse())
    print(dll.search(1)) 
    print(dll.search(4)) 
