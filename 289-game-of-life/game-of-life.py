class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        new = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        for r in range(len(board)):
            for c in range(len(board[0])):
                num_neighbours = 0
                for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 1:
                        num_neighbours += 1
                if board[r][c] == 1:
                    if 2 <= num_neighbours <= 3:
                        new[r][c] = 1
                    else:
                        new[r][c] = 0
                elif num_neighbours == 3:
                    new[r][c] = 1
        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] = new[r][c]