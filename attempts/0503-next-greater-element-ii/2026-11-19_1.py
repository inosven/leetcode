# LC 503 Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/
# 日期: 2026-11-19 | 章节: 单调栈 | 结果: A | 用时: 10min

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack =[]
        n = len(nums)
        ans = [-1] * n
        i = 0
        for i in range(2*n):
            cur = nums[i%n]
            while stack and cur > nums[stack[-1]]:
                ix = stack.pop()
                ans[ix] = cur

            stack.append(i%n)
        return ans
