# LC 322 Coin Change
# https://leetcode.com/problems/coin-change/
# 完全背包 1D：j 正序（dp[j-c] 已是本轮值 → 同一枚硬币可再用）。O(n*amount) / O(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        dp = [INF] * (amount+1)
        dp[0] = 0
        for c in coins:
            for j in range(c, amount+1):
                dp[j] = min(dp[j], dp[j-c] + 1)
        return dp[amount] if dp[amount] != INF else -1
