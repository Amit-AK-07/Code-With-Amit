#User function Template for python3

class Solution:

    def longestPalinSubseq(self, s):
        # code here
        n = len(s)
        dp = [[1]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + (dp[i+1][j-1] if i+1 <= j-1 else 0)
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][-1]