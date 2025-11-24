class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        for c in range(1, len(grid)):
            diagonals = []
            r = 0
            for currC in range(c, len(grid)):
                diagonals.append(grid[r][currC])
                r += 1
            diagonals.sort()
            r = 0
            for currC in range(c, len(grid)):
                grid[r][currC] = diagonals[r]
                r += 1
        for r in range(0, len(grid)):
            diagonals = []
            c = 0
            for currR in range(r, len(grid)):
                diagonals.append(grid[currR][c])
                c += 1
            diagonals.sort(reverse=True)
            c = 0
            for currR in range(r, len(grid)):
                grid[currR][c] = diagonals[c]
                c += 1
        return grid

