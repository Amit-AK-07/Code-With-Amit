#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr):
        # code here
        i = 0
        
        for j in range(len(arr)):
            if arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
