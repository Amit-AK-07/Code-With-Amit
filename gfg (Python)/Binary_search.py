#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        start, end = 0, len(arr) - 1
        
        while start <= end:
            mid = start + (end - start) // 2;
            
            if arr[mid] < k:
                start = mid + 1
                
            elif arr[mid] == k:
                if mid == 0 or arr[mid - 1] != k:
                    return mid
                    
                end = mid - 1
                
            else:
                end = mid - 1
                
        return -1

