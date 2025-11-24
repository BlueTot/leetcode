class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        new = []
        seen = set()
        dr, dc = (0, 1)
        r, c = 0, 0
        while len(seen) < len(matrix)*len(matrix[0]):
            new.append(matrix[r][c])
            seen.add((r,c))
            nr, nc = (r+dr, c+dc)
            if (nr, nc) in seen or not (0 <= nr < len(matrix) and 0 <= nc < len(matrix[0])):
                if (dr, dc) == (0, 1):
                    dr, dc = 1, 0
                elif (dr, dc) == (1, 0):
                    dr, dc = 0, -1
                elif (dr, dc) == (0, -1):
                    dr, dc = -1, 0
                else:
                    dr, dc = 0, 1
            r, c = r+dr, c+dc
        return new
            
                