# LC 40 Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/
# 排序 + 回溯：同层去重 i > start；排序后和超了直接 break。

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        ans = []
        candidates.sort()
        def bt(start,s):
            if s == target:
                ans.append(path[:])
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if s + candidates[i] > target:
                    break
                path.append(candidates[i])
                bt(i+1,s + candidates[i])
                path.pop()
        bt(0,0)
        return ans
