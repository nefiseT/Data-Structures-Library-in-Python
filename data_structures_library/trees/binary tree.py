
""" generic binmary tree + traversals """

class BinaryTreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = BinaryTreeNode(root_value)

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
    bt = BinaryTree(1)
    bt.root.left = BinaryTreeNode(2)
    bt.root.right = BinaryTreeNode(3)
    bt.root.left.left = BinaryTreeNode(4)

    print( "inorde : " , bt.inorder())