class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        M = 10**9 + 7
        
        # grid[i][j] = (smallest, largest)
        # smallest is the minimum product ending at that square
        # largest is the maximum product ending at that square

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    smallest = largest = grid[i][j]
                
                elif i == 0:
                    smallest = min(
                        grid[i][j-1][0] * grid[i][j],
                        grid[i][j-1][1] * grid[i][j]
                    )
                    largest = max(
                        grid[i][j-1][0] * grid[i][j],
                        grid[i][j-1][1] * grid[i][j]
                    )

                elif j == 0:
                    smallest = min(
                        grid[i-1][j][0] * grid[i][j],
                        grid[i-1][j][1] * grid[i][j]
                    )
                    largest = max(
                        grid[i-1][j][0] * grid[i][j],
                        grid[i-1][j][1] * grid[i][j]
                    )

                else:
                    smallest = min(
                        grid[i-1][j][0] * grid[i][j], 
                        grid[i-1][j][1] * grid[i][j], 
                        grid[i][j-1][0] * grid[i][j],
                        grid[i][j-1][1] * grid[i][j]
                    )
                    largest = max( 
                        grid[i-1][j][0] * grid[i][j],
                        grid[i-1][j][1] * grid[i][j],
                        grid[i][j-1][0] * grid[i][j],
                        grid[i][j-1][1] * grid[i][j]
                    )
                grid[i][j] = (smallest, largest)
        
        best = max(grid[m-1][n-1])
        if best >= 0:
            return best % M
        else:
            return -1