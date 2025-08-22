import numpy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # took hint - reverse columns and transpose

        # reverse
        for col in range(len(matrix[0])):
            for row in range(len(matrix)//2): 
                matrix[row][col], matrix[len(matrix)-1-row][col] = matrix[len(matrix)-1-row][col], matrix[row][col]

        # transpose
        for row in range(len(matrix)):
            for col in range(row, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        


        