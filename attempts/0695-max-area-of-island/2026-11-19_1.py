# LC 695 Max Area of Island
# https://leetcode.com/problems/max-area-of-island/
# 日期: 2026-11-19 | 章节: 图论 | 结果: B | 用时: 15min

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])    
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = [[False] * cols for _ in range(rows)]
        def bfs(i,j):
            stack =[]
            if grid[i][j] == 1 and not visited[i][j]:
                area = 1
                stack.append((i,j))
            while stack:
                r , c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr<0 or nr >= rows or nc < 0 or nc >=cols:
                        continue
                    
                    if  grid[nr][nc] ==1 and not visited[nr][nc]:
                        stack.append((nr,nc))
                        area+=1
            return area

        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] ==1 and not visited[i][j]:
                    area = bfs(i,j)
                    maxArea = max(maxArea, area)
        return maxArea
