"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""

from collections import deque
class Solution:
    def levelOrder(self, root):
        # Your code here
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
            result.append(current_level)
            
        return result
