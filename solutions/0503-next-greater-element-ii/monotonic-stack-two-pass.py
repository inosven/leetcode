# LC 503 Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/
# 单调栈 + 遍历两遍模拟环形。栈存下标；第二圈只负责弹出，不再入栈。O(n) / O(n)

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack =[]
        n = len(nums)
        ans = [-1] * n
        for i in range(2*n):
            cur = nums[i%n]
            while stack and cur > nums[stack[-1]]:
                ix = stack.pop()
                ans[ix] = cur
            if i < n:
                stack.append(i)
        return ans
