"""
Doubly Linked List
Allows bidirectional traversal
"""
from node import DoublyNode

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self,data):
        node = DoublyNode(data)
        node.next = self.head 

        if self.head:
            self.head.prev = node

        self.head = node

    def delete(self,key):
        curr = self.head

        while curr:
            if curr.data == key:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                if curr.next:
                    curr.next.prev = curr.prev
                return True
            curr = curr.next
        return False
    
############
#with operations we change what a pointer points to, not the value
#b <-> c <-> d , delete c and it becomes b <-> d 
############

## traverse = each node one by one - repeatedly
    def traverse_forward(self):
        result =[]
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    def traverse_backward(self):
        result = []
        curr = self.head
        if not curr:
            return result
        
        while curr.next:
            curr = curr.next

        while curr:
            result.append(curr.data)
            curr = curr.prev
        return result
    
if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.insert_head(3)
    dll.insert_head(2)
    dll.insert_head(1)

    print("Forwrd:", dll.traverse_forward())
    print("Backward:", dll.traverse_backward())

    dll.delete(2)

    print("----After deletint 2----")
    print("Forward:", dll.traverse_forward())
    print("Backward:", dll.traverse_backward())