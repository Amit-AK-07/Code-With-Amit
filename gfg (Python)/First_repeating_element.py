#User function Template for python3
from collections import defaultdict

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr):
        count = defaultdict(int)
        n = len(arr)
        
        for num in arr:
            count[num] += 1
            
        for i in range(n):
            if(count[arr[i]] >= 2):
                return i+1
        return -1
        #arr : given array
        #n : size of the array