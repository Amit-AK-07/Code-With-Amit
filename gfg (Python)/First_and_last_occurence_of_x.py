#User function Template for python3
class Solution: 
    def firstAndLast(self, x, arr): 
        # Code here
        n = len(arr)
        if x in arr:
            return [arr.index(x), n -1- arr[::-1].index(x)]
        return [-1]


