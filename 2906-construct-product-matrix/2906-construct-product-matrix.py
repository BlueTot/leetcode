class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n, m = len(grid), len(grid[0])
        M = 12345

        product_left = [1 for _ in range(n*m)]
        product_right = [1 for _ in range(n*m)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                idx = i*m + j
                if idx == 0:
                    product_left[idx] = grid[i][j] % M
                else:
                    product_left[idx] = (product_left[idx-1] * grid[i][j]) % M

        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                idx = i*m + j
                if idx == n*m-1:
                    product_right[idx] = grid[i][j] % M
                else:
                    product_right[idx] = (product_right[idx+1] * grid[i][j]) % M
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                idx = i*m + j
                left = idx - 1
                right = idx + 1

                if idx == 0:
                    grid[i][j] = product_right[right]
                elif idx == n*m-1:
                    grid[i][j] = product_left[left]
                else:
                    grid[i][j] = (product_left[left] * product_right[right]) % M
        
        return grid