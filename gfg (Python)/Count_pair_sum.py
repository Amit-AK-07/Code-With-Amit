#User function Template for python3

class Solution:
    def countPairs(self,arr1, arr2, x):
        #code here.
        s = set(arr2)
        count = 0
     
        for i in arr1:
            if x - i in s:
                count += 1
                
        return count