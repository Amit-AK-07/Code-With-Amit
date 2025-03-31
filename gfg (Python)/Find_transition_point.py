class Solution:
    def transitionPoint(self, arr): 
        # Code here
        start, end = 0, len(arr) - 1
        transition = -1
        
        while start <= end:
            mid = (start + end) // 2
            if (arr[mid] == 1):
                transition = mid
                end = mid - 1
            else:
                start = mid + 1
        return transition