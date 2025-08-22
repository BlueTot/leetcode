class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        seen = set()
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        for char, word in zip(pattern, words):
            if char not in mapping:
                if word in seen: return False
                mapping[char] = word
                seen.add(word)
            elif mapping[char] != word:
                return False
        return True