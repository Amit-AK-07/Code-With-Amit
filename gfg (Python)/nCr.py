class Solution:
    def nCr(self, n, r):
        # code here
        if n < r:
            return 0
        
        if r == 0 or r == n:
            return 1
            
        ans = 1
        for i in range(1, r+1):
            ans = ans * (n - r + i) // i
        return ans
