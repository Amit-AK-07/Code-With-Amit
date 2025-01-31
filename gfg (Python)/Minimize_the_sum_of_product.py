#User function Template for python3

class Solution:
    def minValue(self, arr1, arr2):
        #code here
        sum = 0
        arr1.sort()
        arr2.sort(reverse = True)
        
        for i in range(0, len(arr1)):
            ans = arr1[i] * arr2[i]
            sum += ans
        return sum
        

