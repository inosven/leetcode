# LC 454 4Sum II
# https://leetcode.com/problems/4sum-ii/
# 日期: 2026-11-19 | 章节: 哈希表 | 结果: A | 用时: 10min

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        def twoSum(nums1,nums2):
            sumtoi = defaultdict(list)
            for i,num1 in enumerate(nums1):
                for j,num2 in enumerate(nums2):
                    s = num1 + num2
                    sumtoi[s].append((i,j))
            return sumtoi
        sumtoi = twoSum(nums1,nums2)

        ans = 0
        for i,num3 in enumerate(nums3):
            for j,num4 in enumerate(nums4):
                target = -(num3+num4)
                size = len(sumtoi[target])
                ans+=size
        return ans
