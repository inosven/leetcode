# LC 452 Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# 贪心：按左端排序，right = 当前这一箭能覆盖的所有气球右端最小值；
# 下一个左端 > right 才需要新的一箭（相切也能射爆，所以用 >）。O(n log n)

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)

        points.sort(key=lambda x:x[0])
        count = 1
        right = points[0][1]
        for i in range(1,n):
            if points[i][0]> right:
                count+=1
                right = points[i][1]
            else:
                right = min(right,points[i][1])
        return count
