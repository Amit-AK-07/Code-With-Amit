class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        n = len(arr)
        start = 0
        mid = 0
        end = n - 1
        
        while mid <= end:
            if (arr[mid] == 0):
                arr[mid], arr[start] = arr[start], arr[mid]
                mid += 1
                start += 1
            
            elif arr[mid] == 2:
                arr[mid], arr[end] = arr[end], arr[mid]
                end -= 1
            
            else:
                mid += 1
            
        return arr
        