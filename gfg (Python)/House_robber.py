#User function Template for python3

class Solution:
    def maximizeMoney(self, N , K):
        # code here 
        count = 0
        
        for i in range(0, N, 2):
            count += 1
            
        return count * K
