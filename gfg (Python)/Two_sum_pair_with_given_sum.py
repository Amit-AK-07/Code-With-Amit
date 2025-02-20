#User function Template for python3
class Solution:
    def twoSum(self, arr, target):
        # code here
        ans = {}
        
        for i, n in enumerate(arr):
            diff = target - n
            
            if diff in ans:
                return [ans[diff], i]
            ans[n] = i
