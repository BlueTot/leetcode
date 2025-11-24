# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        upper, lower = n, 1
        while True:
            if (res := guess(g := (upper+lower)//2)) == 0:
                return g
            elif res == 1:
                orig_lower = lower
                lower = (upper+lower)//2
                if orig_lower == lower:
                    lower += 1
            else:
                orig_upper = upper
                upper = (upper + lower)//2
                if orig_upper == upper:
                    upper -= 1
        