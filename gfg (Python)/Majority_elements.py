#User function template for Python 3
from collections import Counter

class Solution:
    def majorityElement(self, arr):
        #Your code here
        n = len(arr)
        count = Counter(arr)
        
        for i in count.keys():
            if count[i] > n/2:
                return i
            
        return -1
        
        
        
        
