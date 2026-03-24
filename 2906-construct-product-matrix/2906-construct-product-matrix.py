class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n, m = len(grid), len(grid[0])
        M = 12345

        res = [[1 for _ in range(m)] for _ in range(n)]

        # left prefix sum and write to result matrix
        curr = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res[i][j] = (res[i][j] * curr) % M
                curr = (curr * grid[i][j]) % M

        # right prefix sum and multiply with result matrix
        curr = 1
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                res[i][j] = (res[i][j] * curr) % M
                curr = (curr * grid[i][j]) % M
        
        return res