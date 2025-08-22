class Solution:

    M = 10**9 + 7

    def expM(self, a : int, x : int) -> int:
        if x == 0:
            return 1
        if x == 1:
            return a
        if x & 1 == 0:
            res = self.expM(a, x >> 1) % Solution.M
            return (res * res) % Solution.M
        else:
            res = self.expM(a, x >> 1) % Solution.M
            return (res * res * a) % Solution.M

    def countGoodNumbers(self, n: int) -> int:
        x = (n + 1 >> 1)
        y = n >> 1
        return (self.expM(5, x) * self.expM(4, y)) % Solution.M
        