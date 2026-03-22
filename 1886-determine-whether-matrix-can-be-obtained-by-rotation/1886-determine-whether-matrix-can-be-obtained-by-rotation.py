class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate90(matrix):
            # transpose matrix
            for i in range(len(mat)):
                for j in range(0, i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            # reverse each row
            for row in matrix:
                row.reverse()
            
            return matrix

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate90(mat)
        
        return False