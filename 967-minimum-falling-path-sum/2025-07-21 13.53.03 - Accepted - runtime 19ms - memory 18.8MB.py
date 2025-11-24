class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        paths = [0 for _ in range(n)]
        for r in range(m):
            new = [0 for _ in range(n)]
            for c in range(n):
                if r == 0:
                    new[c] = matrix[r][c]
                else:
                    if c == 0:
                        new[c] = matrix[r][c] + min(paths[c], paths[c+1])
                    elif c == n-1:
                        new[c] = matrix[r][c] + min(paths[c], paths[c-1])
                    else:
                        new[c] = matrix[r][c] + min(paths[c], paths[c+1], paths[c-1])
            paths = new
        return min(paths)