from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        num_cells = 0
        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                if grid[r][c] == 2:
                    queue.append(((r, c), 0))
                if grid[r][c] == 2 or grid[r][c] == 1:
                    num_cells += 1
        
        visited = set()
        mins = set()
        while queue:
            curr, minutes = queue.popleft()
            if curr not in visited:
                visited.add(curr)
                mins.add(minutes)
                for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nr, nc = curr[0]+dr, curr[1]+dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        queue.append(((nr, nc), minutes+1))
        
        if len(visited) == num_cells:
            if len(mins) == 0:
                return 0
            return max(mins)
        return -1
            
            
        