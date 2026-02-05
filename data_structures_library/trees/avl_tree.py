""" self balancing """

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, value):
        if not root:
            return AVLNode(value)
        
        if  value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root) 

# left lft
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)
        
#right right
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)
        
#left right
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

#right left
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def left_rotate(self, z):
        y = z.right
        z.right = y.left
        y.left = z
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y
    
    def right_rotate(self, z):
        y = z.left
        z.left = y.right
        y.right = z
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y
    
    def height (self, node):
        return node.height if node else 0
    
    def balance(self, node):
        return self.height(node.left) - self.height(node.right)
                                            
if __name__ == "__main__":
    avl = AVLTree()
    root = None 
    for v in [23,54,23,5,434,65,34,21]:
        root = avl.insert(root, v)

    print("avl root: ", root.value) 