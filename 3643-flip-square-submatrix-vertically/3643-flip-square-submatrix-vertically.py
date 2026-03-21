class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        for column in range(y, y + k):
            for i in range(0, k//2):

                # swap cells
                j = k - 1 - i
                grid[x+i][column], grid[x+j][column] = grid[x+j][column], grid[x+i][column]
        
        return grid