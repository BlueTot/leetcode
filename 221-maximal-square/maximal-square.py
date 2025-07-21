class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        lengths = [[0 for _ in range(n)] for _ in range(m)]
        largest = 0
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    lengths[r][c] = 1 if matrix[r][c] == "1" else 0
                elif matrix[r][c] == "1":
                    lengths[r][c] = min(lengths[r-1][c], lengths[r][c-1], lengths[r-1][c-1]) + 1
                largest = max(largest, lengths[r][c] ** 2)
        return largest
