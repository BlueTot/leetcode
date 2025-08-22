class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        num = 0
        while (a != 0 or b != 0 or c != 0):
            x1, x2, x3 = a & 1, b & 1, c & 1
            if (x1 == 0 and x2 == 0 and x3 == 0):
                pass
            elif (x1 == 0 and x2 == 0 and x3 == 1):
                num += 1
            elif (x1 == 0 and x2 == 1 and x3 == 0):
                num += 1
            elif (x1 == 0 and x2 == 1 and x3 == 1):
                pass
            elif (x1 == 1 and x2 == 0 and x3 == 0):
                num += 1
            elif (x1 == 1 and x2 == 0 and x3 == 1):
                pass
            elif (x1 == 1 and x2 == 1 and x3 == 0):
                num += 2
            elif (x1 == 1 and x2 == 1 and x3 == 1):
                pass
            a >>= 1
            b >>= 1
            c >>= 1
        return num