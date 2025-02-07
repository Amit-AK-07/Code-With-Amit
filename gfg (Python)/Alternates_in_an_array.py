#User function Template for python3
class Solution:
    def getAlternates(self, arr):
        # Code Here
        ans = []
        n = len(arr)
        for i in range(0, n, 2):
            ans.append(arr[i])
            
        return ans
