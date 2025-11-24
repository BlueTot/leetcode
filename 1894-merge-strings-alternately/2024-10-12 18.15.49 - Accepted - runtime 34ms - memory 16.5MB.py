class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        for i in range(l := (len(word1) if len(word1) < len(word2) else len(word2))):
            output += word1[i] + word2[i]
        output += (word2 if len(word1) < len(word2) else word1)[l:]
        return output