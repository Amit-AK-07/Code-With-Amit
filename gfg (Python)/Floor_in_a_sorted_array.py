class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,k):
        #Your code here
        start, end = 0, len(arr) - 1
        ans = -1  
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if arr[mid] <= k: 
                ans = mid
                start = mid + 1 
            else:
                end = mid - 1 
                
        return ans
