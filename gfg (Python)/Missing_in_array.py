#User function Template for python3
from typing import List

class Solution:
    def missingNumber(self, arr):
        n = len(arr) + 1
        total_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        
        return total_sum - actual_sum
          
