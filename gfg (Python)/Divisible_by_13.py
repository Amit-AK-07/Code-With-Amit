class Solution:
    def divby13(self, s):
        # code here 
        rem = 0
        
        for i in s:
            rem = (rem * 10 + int(i)) % 13
            
        return rem == 0