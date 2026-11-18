# LC 1143 Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
# 日期: 2026-11-17 | 章节: 动态规划 | 结果: C | 用时: 15min

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] the LCS when consider text1 0-j / text2 0-j
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        

        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                elif text1[i-1] == text2[j-2] or text1[i-2] ==text2[j-1]:
                    dp[i][j]  = max(dp[i][j-1], dp[i-1][j]) + 1
                else:
                    dp[i][j] = dp[i-1][j-1]
        return dp[m][n]
