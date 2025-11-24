class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        array = [[None for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if i == 0 or j == 0:
                    array[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    array[i][j] = 1 + array[i-1][j-1]
                else:
                    array[i][j] = max(array[i-1][j], array[i][j-1])
        return array[len(text1)][len(text2)]
        