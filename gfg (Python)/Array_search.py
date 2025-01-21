#User function Template for python3

class Solution:
    #Complete the below function
    def search(self,arr, x):
        #Your code here
        n = len(arr)
        
        for i in range(n):
            if (arr[i] == x):
                return i
        return -1
