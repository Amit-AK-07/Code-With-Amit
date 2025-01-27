#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        n = len(arr)
        
        for i in range(n):
            if arr[i] == k:
                return True
        return False
