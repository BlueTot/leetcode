from functools import cache

class Solution:

    @cache
    def minDistance(self, word1: str, word2: str) -> int:

        # base cases
        if word1 == word2: return 0 # if the same, distance is 0
        if not word1 and word2: return len(word2) # if first is empty, we insert all
        if word1 and not word2: return len(word1) # if second is empty, we delete all

        # recursive cases
        if word1[0] == word2[0]: # the same character, we skip it
            return self.minDistance(word1[1:], word2[1:])
        else: # otherwise we have three options
            replace = self.minDistance(word1[1:], word2[1:])
            insert = self.minDistance(word1, word2[1:])
            remove = self.minDistance(word1[1:], word2)
            return 1 + min(replace, insert, remove)
        