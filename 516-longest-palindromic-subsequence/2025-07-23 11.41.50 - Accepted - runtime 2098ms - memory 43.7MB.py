class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        n = len(s)
        
        # longest common subsequence for s[:i], t[:j]
        lcs = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    continue
                elif s[i-1] == t[j-1]:
                    lcs[i][j] = lcs[i-1][j-1] + 1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        
        return lcs[n][n]