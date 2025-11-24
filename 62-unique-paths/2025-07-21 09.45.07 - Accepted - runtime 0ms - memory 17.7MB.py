class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if (r, c) == (0, 0):
                    ways[r][c] = 1
                elif r == 0:
                    ways[r][c] = ways[r][c-1]
                elif c == 0:
                    ways[r][c] = ways[r-1][c]
                else:
                    ways[r][c] = ways[r-1][c] + ways[r][c-1]
        return ways[m-1][n-1]