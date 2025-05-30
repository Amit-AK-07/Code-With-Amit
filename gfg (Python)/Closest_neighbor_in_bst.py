
class Solution:
    def findMaxFork(self, root, k):
        #code here
        ans = -1
        
        while(root):
            if(root.data == k):
                ans = k
                break
            
            if(root.data < k):
                ans = root.data
                root = root.right
            else:
                root = root.left
            
        return ans