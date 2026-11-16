# LC 454 4Sum II
# https://leetcode.com/problems/4sum-ii/
# 日期: 2026-11-14 | 章节: 哈希表 | 结果: A | 用时: 15min

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        def twoSum(nums1,nums2):
            count=defaultdict(int)
            for num1 in nums1:
                for num2 in nums2:
                    s = num1+num2
                    count[s] = count.get(s,0)+1
        
            return count
        count = twoSum(nums1,nums2)
        count2 = twoSum(nums3,nums4)
        ans = 0
        for s, c in count.items():
            ans += c*count2.get(-s,0)
        return ans
