from typing import List


class Solution:
    def chocolates(self, n : int, arr : List[int]) -> int:
        # code here
        ans = float('inf')
        
        for i in arr:
            if(i < ans):
                ans = i
                
        return ans
        

