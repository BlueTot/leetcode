class Solution:

    def __get(self, mat, r, c):
        if 0 <= r < len(mat) and 0 <= c < len(mat[0]):
            return mat[r][c]
        return 0

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for r in range(len(prefix)):
            for c in range(len(prefix[0])):
                prefix[r][c] = self.__get(prefix, r-1, c) + self.__get(prefix, r, c-1) - self.__get(prefix, r-1, c-1) + mat[r][c]
                
        answer = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for r in range(len(answer)):
            for c in range(len(answer[0])):
                r1 = max(0, r-k)
                c1 = max(0, c-k)
                r2 = min(len(answer)-1, r+k)
                c2 = min(len(answer[0])-1, c+k)
                answer[r][c] = self.__get(prefix, r2, c2) - self.__get(prefix, r2, c1-1) - self.__get(prefix, r1-1, c2) + self.__get(prefix, r1-1, c1-1)
        return answer