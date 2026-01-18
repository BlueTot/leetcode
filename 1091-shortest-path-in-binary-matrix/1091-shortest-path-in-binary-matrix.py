from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        queue = deque([(0, 0)])
    
        if grid[0][0] != 0:
            return -1
        
        while queue:
            r, c = queue.popleft()
            if (r, c) == (len(grid)-1, len(grid[0])-1):
                return grid[r][c] + 1
            
            for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0:
                    queue.append((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1
            
        return -1