class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n > 0:
            total += n % 2
            n //= 2
        return total