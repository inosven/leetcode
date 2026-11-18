# LC 18 4Sum
# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                remain = target - (nums[i] + nums[j])
                # 剪枝：剩下两数的最小和都超了，更大的 j 只会更差
                if nums[j + 1] + nums[j + 2] > remain:
                    break
                # 剩下两数的最大和都不够，换下一个 j
                if nums[n - 2] + nums[n - 1] < remain:
                    continue

                while left < right:
                    cur = nums[left] + nums[right]
                    if cur > remain:
                        right -= 1
                    elif cur < remain:
                        left += 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return ans
