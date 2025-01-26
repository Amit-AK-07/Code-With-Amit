#User function Template for python3

class Solution:
    def check (self,s):
        # your code here
        n = len(s)
        for i in range(n -1):
            if s[i] != s[i + 1]:
                return False
                
        return True
