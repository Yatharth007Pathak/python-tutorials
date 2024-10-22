class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

# Creating a simple binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder_traversal(root)  # Output: 4 2 5 1 3



# Binary Tree Traversal

'''
Recursive Data Structures
Recursion is useful for traversing recursive data structures like trees.
'''