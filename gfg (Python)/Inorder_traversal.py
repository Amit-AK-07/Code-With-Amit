
'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self,root):
        # code here
        ans = []
        self.inorder_traversal(root, ans)
        return ans
    
    def inorder_traversal(self, node, ans):
        if node:
            self.inorder_traversal(node.left, ans)
            ans.append(node.data)
            self.inorder_traversal(node.right, ans)
