class Solution:
    def countStrings(self, s): 
        #code here
        from collections import Counter
        count = Counter(s)
        n = len(s)
        ret = dup = 0
        
        for i in count:
            dup += count[i] > 1
            n -= count[i]
            ret += count[i] * n
            
        return ret + (dup > 0)
            