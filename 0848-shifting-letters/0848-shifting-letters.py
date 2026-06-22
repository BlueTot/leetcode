class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        prefix = 0
        res = [0]*len(s)

        def shift(c, amount):
            return chr((ord(c) - ord('a') + amount) % 26 + ord('a'))

        for i in range(len(shifts)-1, -1, -1):
            val = (shifts[i] + prefix) % 26
            prefix += shifts[i]
            shifts[i] = val
            res[i] = shift(s[i], shifts[i])
        
        return "".join(res)    
        