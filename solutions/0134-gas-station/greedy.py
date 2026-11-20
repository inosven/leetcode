# LC 134 Gas Station
# https://leetcode.com/problems/gas-station/
# 贪心：从 ans 出发累计油量在 i 处变负 → [ans, i] 都不能当起点，起点跳到 i+1。
# 总油量 >= 总消耗时一定有解，最后的 ans 就是答案。O(n)

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
