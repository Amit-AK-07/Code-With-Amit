class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
        n = len(arr)
        ans = [0] * (n+1)
        
        for i in arr:
            ans[i] += 1
            
        return ans[1:]


