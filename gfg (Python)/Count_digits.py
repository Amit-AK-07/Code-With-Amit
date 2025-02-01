#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        count = 0
        num_str = str(n)
        
        for i in num_str:
            i = int(i)
            
            if (i != 0 and n % i == 0):
                count += 1
                
        return count