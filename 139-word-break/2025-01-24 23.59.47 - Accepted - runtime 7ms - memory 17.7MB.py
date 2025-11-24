class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        represented = [None for _ in range(len(s))]
        words = set(wordDict)
        for i in range(len(s)):
            represented[i] = s[:i+1] in words or any(represented[j-1] and s[j:i+1] in words for j in range(i+1))
        return represented[len(s)-1]