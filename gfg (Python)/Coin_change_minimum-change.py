class Solution:
    def minCoins(self, coins, sum):
        # code here
        dp = [float('inf')] * (sum + 1)
        dp[0] = 0  
        
        for coin in coins:
            for j in range(coin, sum + 1):
                dp[j] = min(dp[j], dp[j - coin] +1)
                
        return dp[sum] if dp[sum] != float('inf') else -1