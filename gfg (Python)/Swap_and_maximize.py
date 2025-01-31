#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        #n = len(arr)
        arr.sort()
        start = 0
        end =  len(arr) - 1
        sum = 0
        
        while(start < end):
            sum = sum + (arr[end] - arr[start])
            start += 1
            end -= 1
            
        return sum * 2
