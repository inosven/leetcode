# LC 416 Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # 处理完前 i 个数后，dp[j] 表示能否凑出 j
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(1, n + 1):
            # 倒序：dp[j - x] 仍是上一轮的值，每个数只用一次
            for j in range(target, nums[i - 1] - 1, -1):
                dp[j] = dp[j - nums[i - 1]] or dp[j]
        return dp[target]
