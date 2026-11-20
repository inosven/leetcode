# LC 134 Gas Station
# https://leetcode.com/problems/gas-station/
# 日期: 2026-11-19 | 章节: 贪心 | 结果: A | 用时: 15min

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n=len(gas)
        diff= [0] * n
        sumgas = 0
        sumcost = 0
        total = 0
        ans = 0

        for i in range(n):
            diff[i] = gas[i]-cost[i]
            total+=diff[i]
            if total < 0:
                ans = i+1
                total =0
            sumgas += gas[i]
            sumcost += cost[i]
        if sumgas < sumcost:
            return -1
        return ans
