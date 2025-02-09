class Solution:
    def findSum(self,A,N): 
        #code here
        min_value = float('inf')
        max_value = float('-inf')
        
        for i in A:
            if i < min_value:
                min_value = i
            if i > max_value:
                max_value = i
                
        return min_value + max_value
