#User function Template for python3
class Solution:
    def revStr (self, s : str) -> str :
        # code here 
        str = ""
        for i in range(len(s) - 1, -1, -1):
            str += s[i]
        return str