class Solution:
    def findExtra(self,a,b):
        #add code here\
        n = len(a)
        
        for i in range(n-1):
            if a[i] != b[i]:
                return i
                
        return n - 1
