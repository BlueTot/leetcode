import re
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        poss = {}
        for i in range(len(s)-10+1):
            ss = s[i:i+10]
            if ss not in poss:
                poss[ss] = 1
            else:
                poss[ss] += 1
        return [k for k, v in poss.items() if v > 1]