class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.__prefix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.__rows = len(matrix)
        self.__cols = len(matrix[0])
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.__prefix[r][c] = self.__get(r-1, c) + self.__get(r, c-1) - self.__get(r-1, c-1) + matrix[r][c]
    
    def __get(self, r, c):
        if 0 <= r < self.__rows and 0 <= c < self.__cols:
            return self.__prefix[r][c]
        return 0
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.__get(row2, col2) - self.__get(row2, col1-1) - self.__get(row1-1, col2) + self.__get(row1-1, col1-1)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)