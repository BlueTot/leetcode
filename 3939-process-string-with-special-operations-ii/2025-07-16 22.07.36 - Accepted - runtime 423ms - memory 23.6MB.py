class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        length = 0
        for char in s:
            if char.islower():
                length += 1
            elif char == "*" and length > 0:
                length -= 1
            elif char == "#":
                length *= 2
            lengths.append(length)
        
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            if k >= lengths[i]:
                return "."
            elif char.islower() and k == lengths[i]-1:
                return s[i]
            elif char == "#":
                k = k % (lengths[i] // 2)
            elif char == "%":
                k = lengths[i] - 1 - k
        
        if k >= len(s): return "."
        return s[k]
                  
        
        