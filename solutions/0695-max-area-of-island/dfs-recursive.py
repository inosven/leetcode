# LC 695 Max Area of Island
# https://leetcode.com/problems/max-area-of-island/
# 递归 DFS：dfs(r,c) 返回以 (r,c) 为根、未访问部分的面积（后序汇总）。
# 先进去再检查；一进来就标 visited；area += dfs(...) 不能丢返回值。
# 递归深度最坏 m*n（50x50 实测 2501 > 默认 1000）。O(mn) / O(mn)

import sys
sys.setrecursionlimit(10000)

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0 or visited[r][c]:
                return 0
            visited[r][c] = True
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea
