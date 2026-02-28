from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n <= 0:
            return False

        x = round(log(n) / log(3), 10)
        return 3**x == n
        
