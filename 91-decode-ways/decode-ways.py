from functools import cache

class Solution:

    def decode(self, n):
        if not n: return -1
        if 1 <= int(n) <= 26:
            return chr(int(n) - 1 + ord('A'))
        return -1
    
    @cache
    def numDecodings(self, s: str) -> int:

        # base case
        if not s:
            return 1
        
        ways = 0

        # first digit
        dec_first = self.decode(s[0])
        if dec_first == -1:
            return 0
        ways += self.numDecodings(s[1:])

        # first two digits
        if len(s) >= 2:
            dec_twice = self.decode(s[:2])
            if dec_twice != -1:
                ways += self.numDecodings(s[2:])

        return ways
        