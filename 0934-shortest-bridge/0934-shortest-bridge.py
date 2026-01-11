from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        def bfs(start):
            queue = deque([start])
            grid[start[0]][start[1]] = 2
            queue2 = deque()
            dists = [[-1 for _ in range(m)] for _ in range(n)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 2:
                        if grid[nr][nc] == 0:
                            queue2.append((nr, nc))
                            dists[nr][nc] = 0
                        else:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))
            return queue2, dists

        def get_edge():
            for r in range(n):
                for c in range(m):
                    if grid[r][c] == 1:
                        return bfs((r, c))
    
        queue, dists = get_edge()
        print(queue)
        
        # print(edge)
        # print(grid)
        
        def bfs2(queue, dists):
            res = []
            while queue:
                r, c = queue.popleft()
                if grid[r][c] == 1 and dists[r][c] > 0:
                    return dists[r][c]
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < m and dists[nr][nc] == -1 and grid[nr][nc] != 2:
                        dists[nr][nc] = 1 + dists[r][c]
                        queue.append((nr, nc))
                # print(queue)
        
        return bfs2(queue, dists)
