class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        odd_s1, even_s1, odd_s2, even_s2 = [], [], [], []

        for i, c in enumerate(s1):
            if i % 2 == 0:
                even_s1.append(c)
            else:
                odd_s1.append(c)
        
        for i, c in enumerate(s2):
            if i % 2 == 0:
                even_s2.append(c)
            else:
                odd_s2.append(c)
        
        return sorted(odd_s1) == sorted(odd_s2) and sorted(even_s1) == sorted(even_s2)