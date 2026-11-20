# LC 496 Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/
# 单调栈：栈里是还没找到下一个更大元素的数（栈底→栈顶递减）。
# num2 把栈顶弹出 → num2 就是被弹出数的答案。O(n + m)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        ans = [-1] * n
        st = []

        ntoi = {n:i for i,n in enumerate(nums1)}

        for num2 in nums2:
            while st and num2 > st[-1]:
                num = st.pop()
                pos = ntoi.get(num, -1)
                if pos != -1:
                    ans[pos] = num2
            st.append(num2)
        return ans
