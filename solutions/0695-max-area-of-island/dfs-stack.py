# LC 695 Max Area of Island
# https://leetcode.com/problems/max-area-of-island/
# 迭代 DFS（显式栈）：压栈时计入面积，同时标 visited。O(mn) / O(mn)

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])    
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = [[False] * cols for _ in range(rows)]
        def dfs(i,j):
            stack =[]
            area = 1
            visited[i][j] = True
            stack.append((i,j))
            while stack:
                r , c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr<0 or nr >= rows or nc < 0 or nc >=cols:
                        continue
                    
                    if  grid[nr][nc] ==1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        stack.append((nr,nc))
                        area+=1
            return area

        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] ==1 and not visited[i][j]:
                    area = dfs(i,j)
                    maxArea = max(maxArea, area)
        return maxArea
