class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b