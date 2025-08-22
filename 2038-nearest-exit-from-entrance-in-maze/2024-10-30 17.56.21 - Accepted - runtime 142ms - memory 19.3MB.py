from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([(tuple(entrance), 0)])
        visited = set()
        while queue:
            curr, steps = queue.popleft()
            if (curr[0] in (0, len(maze)-1) or curr[1] in (0, len(maze[0])-1)) and curr != tuple(entrance):
                return steps
            if curr not in visited:
                visited.add(curr)
                for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nr, nc = curr[0]+dr, curr[1]+dc
                    if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != "+":
                        queue.append(((nr, nc), steps+1))
        return -1
        