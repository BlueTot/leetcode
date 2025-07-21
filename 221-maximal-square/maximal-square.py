class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        areas = [[0 for _ in range(n)] for _ in range(m)]
        largest = 0
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    areas[r][c] = 1 if matrix[r][c] == "1" else 0
                elif matrix[r][c] == "1":
                    areas[r][c] = min(areas[r-1][c], areas[r][c-1], areas[r-1][c-1]) + 1
                largest = max(largest, areas[r][c] ** 2)
        return largest
