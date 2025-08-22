class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        output = 0
        for r in range(len(grid)):
            for c in range(len(grid)):
                for i in range(len(grid)):
                    if grid[r][i] != grid[i][c]:
                        break
                else:
                    output += 1
        return output

