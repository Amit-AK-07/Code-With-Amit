class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        count_0 = arr.count(0)
        count_1 = arr.count(1)
        count_2 = arr.count(2)
        
        
        
        
        
        arr[:] = [0] * count_0 + [1] * count_1 + [2] * count_2
        