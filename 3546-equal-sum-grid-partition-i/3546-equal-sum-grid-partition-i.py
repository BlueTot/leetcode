class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        total_sum = sum([sum(row) for row in grid])
    
        top_sum, bottom_sum = 0, total_sum
        for i in range(m-1):

            row_sum = sum(grid[i])
            top_sum += row_sum
            bottom_sum -= row_sum

            if top_sum == bottom_sum:
                return True
        
        left_sum, right_sum = 0, total_sum
        for j in range(n-1):

            col_sum = 0
            for i in range(m):
                col_sum += grid[i][j]
            left_sum += col_sum
            right_sum -= col_sum

            if left_sum == right_sum:
                return True

        return False