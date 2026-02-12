from math import log2

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n == 0:
            return False
        if n == 1:
            return True
        
        pos = int(log2(n & (-n)))
        n = n & (n-1) # clear last

        return n == 0 and pos % 2 == 0