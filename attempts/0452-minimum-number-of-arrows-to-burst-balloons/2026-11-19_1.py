# LC 452 Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# 日期: 2026-11-19 | 章节: 贪心 | 结果: A | 用时: 15min

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
