class Solution:
    def subarraySum(self, arr):
        # code here 
        n = len(arr)
        sum = 0
        
        for i in range(n):
            a = (i + 1) * (n - i)
            sum += a * arr[i]
            
        return sum
        