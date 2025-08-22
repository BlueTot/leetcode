class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def exists(k, r, c, path):
            # print(k, r, c, board[r][c], word[k], path)
            if board[r][c] != word[k]: return False
            if k == len(word) - 1: return True
            for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                nr, nc = r+dr, c+dc
                path.add((r,c))
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and \
                    (nr, nc) not in path and exists(k+1, nr, nc, path):
                        return True
                path.remove((r,c))
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    # print("doing", r, c, word[0])
                    if exists(0, r, c, set([(r,c)])):
                        # print(r,c)
                        return True
        return False