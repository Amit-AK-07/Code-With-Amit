#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        n = len(arr)
        start = 0
        end = n - 1
        ans = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if arr[mid] == k:
                ans = mid
                end = mid - 1
            elif arr[mid] < k:
                start = mid + 1
            else:
                end = mid - 1
                
        return ans

