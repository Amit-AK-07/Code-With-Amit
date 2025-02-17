#User function Template for python3
class Solution:
    def printString(self, s, ch, count):
        # code here
        c = 0
        n = len(s)
        
        for i in range(n):
            if s[i] == ch:
                c += 1
                
            if c == count:
                return s[i + 1 : ]
                break
        
        return ""