#User function Template for python3

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Code here
        if root is None:
            return
    
        # Swap the left and right subtrees
        root.left, root.right = root.right, root.left
        
        # Recursively call the function on left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
