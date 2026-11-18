# LC 416 Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # dp[i][j]：只用前 i 个数（每个最多一次），能否凑出 j
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
        return dp[n][target]
