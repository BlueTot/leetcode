class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        old_divisor = divisor
        while (divisor << 1) <= dividend:
            divisor <<= 1
        quotient = 0
        while (divisor >= old_divisor):
            if (diff := dividend - divisor) >= 0:
                dividend -= divisor
                quotient |= 1
            divisor >>= 1
            quotient <<= 1
        quotient = (-1 if sign else 1) * quotient >> 1
        if quotient > (v := 2**31 - 1):
            return v
        if quotient < (v := -2**31):
            return v
        return quotient
