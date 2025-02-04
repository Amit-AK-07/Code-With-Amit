'''
# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    
    def solve(self, node, diameter):
        if not node:
            return 0
        
        left_height = self.solve(node.left, diameter)
        right_height = self.solve(node.right, diameter)
        
        diameter[0] = max(diameter[0], left_height + right_height + 1)
        
        return 1 + max(left_height, right_height)
    
    
    def diameter(self, root):
        # Your code here
        if not root:
            return 0
            
        diameter = [0]
        self.solve(root, diameter)
        
        return diameter[0] - 1
        
        
