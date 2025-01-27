#User function Template for python3
class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        ans = []
        n = len(arr)
        
        for i in range(1, n + 1):
            if arr[i-1] == i:
                ans.append(i)
        return ans
