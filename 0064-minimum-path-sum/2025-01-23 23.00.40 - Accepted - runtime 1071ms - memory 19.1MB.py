from functools import lru_cache

class Solution:

    @lru_cache
    def minDist(self, row, col):
        if row == 0 and col == 0:
            return self.grid[row][col]
        if col == 0 and row != 0:
            return self.minDist(row-1, col) + self.grid[row][col]
        if row == 0 and col != 0:
            return self.minDist(row, col-1) + self.grid[row][col]
        return min(self.minDist(row-1, col), self.minDist(row, col-1)) + self.grid[row][col]

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        return self.minDist(len(grid)-1, len(grid[0])-1)
        