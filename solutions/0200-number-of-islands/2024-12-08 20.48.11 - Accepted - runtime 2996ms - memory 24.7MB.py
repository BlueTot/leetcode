from collections import deque
from random import randint
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        locations = set()
        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                if grid[r][c] == "1":
                    locations.add((r, c))
        while locations:
            queue = deque([list(locations)[0]])
            while queue:
                r, c = queue.popleft()
                if (r, c) in locations:
                    locations.remove((r, c))
                    for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) in locations and grid[nr][nc] == "1":
                            queue.append((nr, nc))
            num_islands += 1
        return num_islands