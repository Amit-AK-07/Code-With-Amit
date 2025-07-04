#User function Template for python3
#User function Template for python3

class Solution:
    def get_min_max(self, arr):
        if arr == 0:
            return None
        
        min_val = max_val = arr[0]
        
        for i in range(len(arr)):
            if arr[i] < min_val:
                min_val = arr[i]
            elif arr[i] > max_val:
                max_val = arr[i]
        
        return min_val, max_val