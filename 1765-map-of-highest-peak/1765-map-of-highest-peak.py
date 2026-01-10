from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
         
        queue = deque()
        n, m = len(isWater), len(isWater[0])

        res = [[-1 for _ in range(m)] for _ in range(n)]

        for r in range(n):
            for c in range(m):
                if isWater[r][c] == 1:
                    queue.append((r, c))
                    res[r][c] = 0
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < m and \
                    isWater[nr][nc] == 0 and res[nr][nc] == -1:
                    res[nr][nc] = 1 + res[r][c]
                    queue.append((nr, nc))
        
        return res

