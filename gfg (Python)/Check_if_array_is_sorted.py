#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        # code here
        n = len(arr)
        
        for i in range(1, n):
            if (arr[i] >= arr[i - 1]):
                pass
            else:
                return 0
        return 1
