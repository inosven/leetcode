# LC 416 Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/
# 日期: 2026-11-17 | 章节: 动态规划 | 结果: B | 用时: 25min
# 版本 1：二维 dp

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # dp[i][j]：考虑前i个数，能否凑出j
        total = sum(nums)
        if total %2!=0:
            return False
        nums.sort()
        target = int(total/2)
        n=len(nums)
        dp = [[0] * (target+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True
        

        for j in range(1,target+1):
            dp[0][j]= False

        if all(nums) is 0:
            return True
        
        for i in range(1,n+1):
            for j in range(1,target+1):
                dp[i][j] = dp[i-1][j]
                if j>nums[i-1]:
                    dp[i][j] = dp[i][j-nums[i-1]] or dp[i-1][j]
        return dp[n][target]
