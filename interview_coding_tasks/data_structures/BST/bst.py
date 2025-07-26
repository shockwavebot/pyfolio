class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None
    
    def insert(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            return
        
        current = self.root
        while True:
            if value < current.val:
                if current.left is None:
                    current.left = node
                    return
                else:
                    current = current.left
            elif value > current.val:
                if current.right is None:
                    current.right = node 
                    return
                else:
                    current = current.right
            else:
                raise ValueError(f"Value {value} already present in BST")
