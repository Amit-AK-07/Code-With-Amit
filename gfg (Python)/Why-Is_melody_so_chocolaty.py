class Solution:
    def max_happiness(self, arr):
        # code here
        n = len(arr)
        if n < 2:
            return 0
            
        max_happy = float('-inf')
        
        for i in range(n - 1):
            sum = arr[i] + arr[i + 1]
            max_happy = max(max_happy, sum)
        return max_happy
