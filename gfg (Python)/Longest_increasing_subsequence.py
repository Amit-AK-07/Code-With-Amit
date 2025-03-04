class Solution:
    def lis(self, arr):
        # code here
        n = len(arr)
        if n == 0:
            return 0
    
        ls = [0] * n  
        ans = 1  
    
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    ls[i] = max(ls[i], ls[j]) 
            ls[i] += 1  
            ans = max(ans, ls[i])  
    
        return ans

