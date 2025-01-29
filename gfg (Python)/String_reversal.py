#User function Template for python3

class Solution:
    def reverseString(self, s):
        # code here
        n = len(s)
        ans = ""
        
        for i in range(n-1, -1, -1):
            if s[i] != " ":
                
                if s[i] not in ans:
                    ans += s[i]

        return ans
