#User function Template for python3

class Solution:
    ##Complete this code
    def countOnes(self,arr, N):
        #Your code here
        count = 0
        
        for i in range(N):
            if arr[i] == 1:
                count += 1
                
        return count
