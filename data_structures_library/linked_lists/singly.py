"""
Singly Linked List

Operations:
- Insert (head, tail)
- Delete
- Search
- Traverse

Time Complexity:
- Insert at head: O(1)
- Insert at tail: O(n)
- Delete/Search: O(n)

"""

from node import SinglyNode

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        node = SinglyNode(data)
        node.next = self.head
        self.head = node

    def insert_tail(self, data):
        node = SinglyNode(data)
        if not self.head:
            self.head = node
            return
        
        curr =self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def delete(self, key):
        curr = self.head

        if curr and curr.data == key:
            self.head = curr.next
            return True
        
        prev = None 
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if curr:
            prev.next = curr.next
            return True
        return False
    
    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            
            curr = curr.next
        return False
    def traverse(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_head(3)
    ll.insert_tail(5)
    ll.insert_tail(7)
    print(ll.traverse())
    ll.delete(5)
    print(ll.traverse())
    


        
