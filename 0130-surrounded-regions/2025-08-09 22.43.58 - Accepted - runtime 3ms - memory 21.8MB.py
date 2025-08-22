from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def get(r, c):
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                return board[r][c]
            return "O"

        queue = deque([(-1, -1)])
        visited = set()
        while queue:
            r, c = queue.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                nr, nc = r+dr, c+dc
                # bounds checking and value checking
                if -1 <= nr <= len(board) and -1 <= nc <= len(board[0]) and \
                  (nr, nc) not in visited and get(nr, nc) == "O":
                  queue.append((nr, nc))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r, c) not in visited:
                    board[r][c] = "X"
 
