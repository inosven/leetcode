# LC 209 Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# 日期: 2026-11-19 | 章节: 数组 | 结果: A | 用时: 10min

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF  = float('inf')
        minlen = INF
        left = 0
        n = len(nums)
        total = 0
        for right in range(n):
            total += nums[right]
            while left <= right and total >= target:
                minlen = min(minlen, right-left+1)
                total-=nums[left]
                left+=1
        return minlen if minlen!=INF else 0
