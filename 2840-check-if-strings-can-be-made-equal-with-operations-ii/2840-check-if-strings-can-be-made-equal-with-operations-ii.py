from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:

        odd_s1 = {}
        even_s1 = {}
        odd_s2 = {}
        even_s2 = {}

        for i, c in enumerate(s1):
            if i % 2 == 0:
                even_s1[c] = even_s1.get(c, 0) + 1
            else:
                odd_s1[c] = odd_s1.get(c, 0) + 1
        
        for i, c in enumerate(s2):
            if i % 2 == 0:
                even_s2[c] = even_s2.get(c, 0) + 1
            else:
                odd_s2[c] = odd_s2.get(c, 0) + 1
        
        return odd_s1 == odd_s2 and even_s1 == even_s2