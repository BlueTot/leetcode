class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        prefix = 0

        for i in range(len(shifts)-1, -1, -1):
            val = (shifts[i] + prefix) % 26
            prefix += shifts[i]
            shifts[i] = val
        
        def shift(c, amount):
            return chr((ord(c) - ord('a') + amount) % 26 + ord('a'))
        
        return "".join([shift(c, shifts[i]) for i, c in enumerate(s)])
        
        
        
        