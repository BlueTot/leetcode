from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def get(heights, r, c):
            if 0 <= r < len(heights) and 0 <= c < len(heights[0]):
                return heights[r][c]
            return 0
        
        def bfs(initial_set):

            visited = set()
            queue = deque(initial_set)

            while queue:
                r, c = queue.popleft()
                if (r,c) in visited:
                    continue
                visited.add((r, c))
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) \
                    and heights[nr][nc] >= get(heights, r, c):
                        queue.append((nr, nc))
            
            return visited
            
        pacific_initial = []
        for i in range(-1, len(heights[0])):
            pacific_initial.append((-1, i))
        for j in range(0, len(heights)):
            pacific_initial.append((j, -1))
        
        pacific = bfs(pacific_initial)

        atlantic_initial = []
        for i in range(-1, len(heights[0])):
            atlantic_initial.append((len(heights), i))
        for j in range(0, len(heights)):
            atlantic_initial.append((j, len(heights[0])))
        
        atlantic = bfs(atlantic_initial)

        return list(pacific & atlantic)