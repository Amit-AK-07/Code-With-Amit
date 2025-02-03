#User function Template for python3

class Solution:
    def countZeroes(self, arr):
        # code here
        count = 0
        
        for i in arr:
            if i == 0:
                count += 1
        return count
