class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lower = 0
        upper = len(matrix)*len(matrix[0])-1
        while lower <= upper:
            mid = (lower+upper)//2
            row, col = mid // len(matrix[0]), mid % len(matrix[0])
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                upper = mid - 1
            else:
                lower = mid + 1
            print(mid, lower, upper, row, col)
        return False