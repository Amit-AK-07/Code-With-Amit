#User function Template for python3


class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,s1,s2):
        #code here
        if len(s1) != len(s2):
            return False
        
        n = len(s1)
        if n < 2:
            return s1 == s2
            
        end = s1[2:] + s1[:2]
        start = s1[-2:] + s1[:-2]
        return s2 == end or s2 == start