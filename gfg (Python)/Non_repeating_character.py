#User function Template for python3
from collections import Counter
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        ans = Counter(s)
        
        for i in s:
            if ans[i] == 1:
                return i
                
        return -1
        
                
    
    
