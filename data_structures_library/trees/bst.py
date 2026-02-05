""" binary search treee """

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = BSTNode(value)

        elif value > node.value:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = BSTNode(value)

    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res
    
    def _inorder(self, node, res):
        if node:
            self._inorder(node.left, res)
            res.append(node.value)
            self._inorder(node.right, res)
            

if __name__ == "__main__":
    bst = BinarySearchTree()
    for v in [50, 30, 70,20, 40, 32, 929]:
        bst.insert(v)

    print("inorder:", bst.inorder())