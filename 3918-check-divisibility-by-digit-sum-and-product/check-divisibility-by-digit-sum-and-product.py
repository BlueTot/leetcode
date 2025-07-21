from functools import reduce

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(i) for i in str(n)]
        digit_sum = sum(digits)
        digit_product = reduce(lambda a, b: a * b, digits)
        return n % (digit_sum + digit_product) == 0