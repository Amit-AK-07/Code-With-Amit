#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        ##Your code here
        n = len(arr)
        ans = {}
        sum = 0
        
        for i in range(n):
            sum += arr[i]
            if sum == 0:
                return True
            
            if sum in ans:
                return True
            ans[sum] = 1
            
        #Return true or false
        return False
