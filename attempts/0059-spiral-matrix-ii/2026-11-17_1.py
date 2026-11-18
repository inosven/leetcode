# LC 59 Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii/
# 日期: 2026-11-17 | 章节: 数组 | 结果: A（初次提交不对，自己改对；此为改后版本）| 用时: 10min

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]

        top = left = 0
        right = bottom = n-1
        i = 1
        while i <= n**2:
            for col in range(left,right+1):
                ans[top][col%n] = i
                i+=1
            top+=1
            
            for row in range(top,bottom+1):
                ans[row%n][right]=i
                i+=1
            right-=1

            for col in range(right,left-1,-1):
                ans[bottom][col%n] = i
                i+=1
            bottom-=1

            for row in range(bottom,top-1,-1):
                ans[row%n][left] = i
                i+=1
            left+=1
        return ans
