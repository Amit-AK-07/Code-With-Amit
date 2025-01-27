#User function Template for python3

class Solution:
    def countZeroes(self, arr):
        # code here
        n = len(arr)
        count = 0
        
        for i in range(n):
            if arr[i] == 0:
                count += 1
                
        return count
