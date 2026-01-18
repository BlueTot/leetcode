class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def bfs(start):
            queue = deque([start])
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        return False
                    elif grid[nr][nc] == 0:
                        queue.append((nr, nc))
                        grid[nr][nc] = 1
            return True
        
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    if bfs((i, j)):
                        res += 1
        
        return res

                    

