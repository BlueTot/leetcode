from functools import cache

class Solution:

    MOD = 10**9 + 7

    @cache
    def numTilings(self, n: int) -> int:

        if n <= 1:
            return 1

        ways = 0

        # vertical domino
        ways += 1 * self.numTilings(n-1)

        # horizontal domino
        ways += 1 * self.numTilings(n-2)

        # tromino
        for i in range(3, n+1):
            ways += 2 * self.numTilings(n-i)
        
        return ways % Solution.MOD