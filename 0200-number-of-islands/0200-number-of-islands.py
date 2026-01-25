from collections import deque

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    queue = deque([(i, j)])
                    grid[i][j] = "0"
                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                            nr, nc = r+dr, c+dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) \
                               and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                queue.append((nr, nc))
                    num_islands += 1
        
        return num_islands