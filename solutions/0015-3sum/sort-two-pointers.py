# LC 15 3Sum
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        ans = []
        nums.sort()
        n = len(nums)
        for i in range(0,n-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            left = i +1
            right = n-1
            while left < right:
                if nums[left] + nums[right] > target:
                    right-=1
                elif nums[left] + nums[right] < target:
                    left+=1

                else:
                    ans.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
        return ans
