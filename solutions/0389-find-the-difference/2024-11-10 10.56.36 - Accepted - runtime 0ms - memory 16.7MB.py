class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1 = sum([ord(c) for c in s])
        sum2 = sum([ord(c) for c in t])
        return chr(abs(sum1 - sum2))