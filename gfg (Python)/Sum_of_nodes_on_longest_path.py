
class Node:
    def __init__(self, val):
        self.data=val
        self.left = None
        self.right = None
        
class Solution:
    
    def preOrder(self, curr, sum_, length, maxLenAndSum):
        if curr is None:
            maxLen, maxSum = maxLenAndSum
            if length > maxLen:
                maxLenAndSum[0] = length
                maxLenAndSum[1] = sum_
            elif length == maxLen:
                maxLenAndSum[1] = max(sum_, maxSum)
            return
        
        self.preOrder(curr.left, sum_ + curr.data, length + 1, maxLenAndSum)
        self.preOrder(curr.right, sum_ + curr.data, length + 1, maxLenAndSum)
        
    def sumOfLongRootToLeafPath(self, root):
        #code here
        maxLenAndSum = [0, 0]
        self.preOrder(root, 0, 0, maxLenAndSum)
        return maxLenAndSum[1]