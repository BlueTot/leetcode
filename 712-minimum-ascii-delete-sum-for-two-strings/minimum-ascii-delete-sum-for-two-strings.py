from functools import cache

class Solution:

    @cache
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        # base cases
        if s1 == s2: return 0 # no deletions required
        if not s1 and s2: return sum(map(ord, s2)) # delete all from s2
        if s1 and not s2: return sum(map(ord, s1)) # delete all from s1

        if s1[0] == s2[0]:
            return self.minimumDeleteSum(s1[1:], s2[1:])
        else:
            first = ord(s1[0]) + self.minimumDeleteSum(s1[1:], s2)
            second = ord(s2[0]) + self.minimumDeleteSum(s1, s2[1:])
            return min(first, second)