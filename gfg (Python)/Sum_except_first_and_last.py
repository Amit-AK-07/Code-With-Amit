#User function Template for python3


class Solution:
    def sumExceptFirstLast(self,arr):
        # Parr:  list of pair
        #code here
        n = len(arr)
        sum = 0
        for i in range(1, n-1):
            sum += arr[i]
        return sum
            