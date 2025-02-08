#User function Template for python3

class Solution:
    def solve(self,n : int, a : list, b : int):
        # Complete this function
        ans = b
        result = set(a)
        
        while ans in result:
            ans *= 2
            
        return ans
