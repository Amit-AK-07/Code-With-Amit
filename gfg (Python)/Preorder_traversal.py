#User function Template for python3



'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
#Function to return a list containing the preorder traversal of the tree.
    def preorder(self,root):
        ans = []
        self.preorder_traversal(root, ans)
        return ans
   
    # code here
    def preorder_traversal(self, node, ans):
        if node:
            ans.append(node.data)
            self.preorder_traversal(node.left, ans)
            self.preorder_traversal(node.right, ans)
