class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0 for _ in range(n)] for _ in range(n)]
        
        r, c = 0, 0
        dr, dc = 0, 1
        for i in range(1, n*n+1):
            nums[r][c] = i
            nr, nc = r+dr, c+dc
            if not(0 <= nr < n and 0 <= nc < n) or nums[nr][nc] != 0:
                if (dr, dc) == (0, 1):
                    dr, dc = (1, 0)
                elif (dr, dc) == (1, 0):
                    dr, dc = (0, -1)
                elif (dr, dc) == (0, -1):
                    dr, dc = (-1, 0)
                else:
                    dr, dc = (0, 1)
            r, c = r+dr, c+dc
            
        return nums