#User function Template for python3
from collections import Counter
from typing import List

class Solution:
    def firstElementKTime(self, arr,k):
        # code here
        ans = Counter()
        
        for num in arr:
            ans[num] += 1
            
            if ans[num] == k:
                return num
        return -1
    

