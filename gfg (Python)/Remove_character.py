#User function Template for python3

class Solution:
    def removeChars (ob, string1, string2):
        # code here
        ans = set(string2)
        result = ''.join(char for char in string1 if char not in ans)
        return result
