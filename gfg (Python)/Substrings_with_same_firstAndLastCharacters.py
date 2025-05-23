class Solution:
    def countSubstring(self, s):
        # code here
        from collections import Counter
        
        freq = Counter(s)
        count = 0
        
        for i in freq.values():
            count += (i * (i+1)) // 2
           
        return count