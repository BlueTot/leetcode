from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        queue = deque()
        n, m = len(mat), len(mat[0])

        res = [[0 for _ in range(m)] for _ in range(n)]

        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0:
                    is_adj = False
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                            is_adj = True
                            break
                    if is_adj:
                        queue.append(((r, c), 0))
        
        visited = set()
        while queue:
            curr, dist = queue.popleft()
            r, c = curr
            if mat[r][c] == 1 and (r, c) not in visited:
                res[r][c] = dist
            visited.add(curr)
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < m and \
                    mat[nr][nc] == 1 and (nr, nc) not in visited:
                    queue.append(((nr, nc), dist + 1))
        
        return res

