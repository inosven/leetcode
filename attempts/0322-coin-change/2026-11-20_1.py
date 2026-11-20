# LC 322 Coin Change
# https://leetcode.com/problems/coin-change/
# 日期: 2026-11-20 | 章节: 动态规划 | 结果: B | 用时: 15min

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i][j] 考虑前i个硬币，凑出j的最小硬笔数量
        n = len(coins)
        dp = [[-1] * (amount+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1,n+1):
            for j in range(1,amount+1):

                if j-coins[i-1]>=0:
                    dp[i][j] = min(dp[i][j-coins[i-1]]+1, dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount]
