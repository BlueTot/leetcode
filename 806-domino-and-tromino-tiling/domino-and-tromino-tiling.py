class Solution:

    MOD = 10**9 + 7

    def numTilings(self, n: int) -> int:

        ways = [0 for _ in range(n+1)]
        ways[0] = 1

        for i in range(1, n+1):
            
            # vertical domino
            ways[i] += ways[max(0, i-1)]

            # horizontal domino
            if i - 2 >= 0:
                ways[i] += ways[i-2]

            # tromino
            for j in range(3, i+1):
                if i - j >= 0:
                    ways[i] += 2 * ways[i-j]
        
            ways[i] %= Solution.MOD

        print(ways)
        return ways[n]