#User function Template for python3
class Solution:
    def arraySum(self, arr):
           # code here
           n = len(arr)
           sum = 0
           
           for i in range(n):
               sum += arr[i]
           return sum

