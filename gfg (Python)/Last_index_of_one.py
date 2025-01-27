#User function Template for python3

class Solution:
    def lastIndex(self, s: str) -> int:
        # code here
        n = len(s)
        index = -1
        
        for i in range(n):
            if s[i] == '1':
                index = i
                
        return index
        

