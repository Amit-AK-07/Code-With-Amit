
class Solution:
    def longest(self, arr):
        # code here
        n = len(arr)
        ans = arr[0]
        
        for i in range(1, n):
            if(len(arr[i]) > len(ans)):
                ans = arr[i]
        return ans
        
