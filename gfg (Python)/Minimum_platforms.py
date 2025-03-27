#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort()
        dep.sort()
    
        n = len(arr)
        i, j = 0, 0
        count = 0
        max_platforms = 0
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            max_platforms = max(max_platforms, count)
        
        return max_platforms
                