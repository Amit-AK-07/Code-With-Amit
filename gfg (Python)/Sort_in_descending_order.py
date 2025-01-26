#User function Template for python3
class Solution:
    def ReverseSort(self, s): 
        # code here
        str = sorted(s, reverse = True)
        ans = "".join(str)
        return ans
