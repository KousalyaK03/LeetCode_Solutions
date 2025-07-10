# Last updated: 7/10/2025, 1:44:44 PM
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))

            grid[i][j] = '0'
            while queue:
                x, y = queue.popleft()
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        queue.append((nx, ny))
                        grid[nx][ny] = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    island_count += 1
                    bfs(i, j)
        return island_count