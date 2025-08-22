from functools import lru_cache

class Solution:

    @lru_cache
    def isPalindrome(self, s):
        return s[::-1] == s

    def longestPalindrome(self, s: str) -> str:
        for length in range(len(s), 0, -1):
            i = 0
            while (end := i + length - 1) <= len(s) - 1:
                if self.isPalindrome(s[i:end+1]):
                    return s[i:end+1]
                i += 1
            