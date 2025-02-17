#User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr):
        # code here
        ans = max(arr)
        currMax, currMin = 1, 1
        n = len(arr)
        
        for i in range(n):
            if arr[i] < 0:
                currMax, currMin = currMin, currMax
            
            currMax = max(arr[i] * currMax, arr[i])
            currMin = min(arr[i] * currMin, arr[i])
            ans = max(ans, currMax)
           
        return ans
