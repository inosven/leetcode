# LC 416 Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/
# 日期: 2026-11-17 | 章节: 动态规划 | 结果: B | 用时: 25min
# 版本 2：一维滚动 dp

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # dp[i][j]：考虑前i个数，能否凑出j
        total = sum(nums)
        if total %2!=0:
            return False
        target = int(total/2)
        n=len(nums)
        dp = [0] * (target+1)

        for i in range(n+1):
            dp[0] = True
        
        
        for i in range(1,n+1):
            for j in range(target+1,nums[i-1]-1,-1):
                dp[j] = dp[j-nums[i-1]] or dp[j]
        return dp[target]
