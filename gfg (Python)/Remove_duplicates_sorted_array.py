#User function template for Python

class Solution:
    def removeDuplicates(self, arr):
        #Code Here
        a = list(set(arr))
        n = len(a)
        a.sort()
        
        for i in range(n):
            arr[i] = a[i]
            
        return n
