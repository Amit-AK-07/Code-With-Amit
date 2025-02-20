#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        #code here
        ans = 0
        i = 0
        
        while i != n + 1:
            ans += i * i * i
            i += 1
            
        return ans
        