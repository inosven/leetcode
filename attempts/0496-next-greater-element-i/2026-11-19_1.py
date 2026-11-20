# LC 496 Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/
# 日期: 2026-11-19 | 章节: 单调栈 | 结果: B | 用时: 10min

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        ans = [-1] * n
        st = []

        ntoi = {n:i for i,n in enumerate(nums1)}

        for num2 in nums2:
            while st and num2>st[-1]:
                num = st.pop
                pos=ntoi.get(num2,-1)
                if pos!=-1:
                    ans[pos] =  num
            st.append(num2)
        return ans
