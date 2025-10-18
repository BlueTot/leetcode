from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(start, seen):
            area = 0
            queue = deque([start])
            while queue:
                curr = queue.popleft()
                if curr in seen:
                    continue
                area += 1
                seen.add(curr)
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = curr[0]+dr, curr[1]+dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        queue.append((nr, nc))
            return area

        
        seen = set()
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs((r, c), seen))
                else:
                    seen.add((r, c))
        
        return max_area
