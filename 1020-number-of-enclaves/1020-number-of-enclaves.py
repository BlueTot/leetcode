class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def bfs(start):
            queue = deque([start])
            is_closed = True
            num_cells = 0
            grid[start[0]][start[1]] = 0
            while queue:
                r, c = queue.popleft()
                num_cells += 1
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        is_closed = False
                    elif grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 0
            return num_cells if is_closed else 0
        
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += bfs((i, j))
        
        return res
