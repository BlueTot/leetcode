from itertools import combinations
from functools import cache
from collections import Counter

class Solution:  

    def countTrapezoids(self, points: List[List[int]]) -> int:

        M = 10**9 + 7

        def nc2modm(n, m):
            return (n * (n - 1) // 2) % m

        groups = {}
        for x, y in points:
            if y not in groups:
                groups[y] = set()
            groups[y].add((x, y))
        
        def choose2counter(counts):
            for a, b in combinations(counts.keys(), 2):
                yield ((a, b), counts[a] * counts[b])
            for n, c in counts.items():
                yield ((n, n), c * (c - 1) // 2)
        
        lengths = Counter([len(v) for v in groups.values() if len(v) >= 2])
        total = 0
        for pair, count in choose2counter(lengths):
            a, b = pair
            if count > 0:
                total += (nc2modm(a, M) * nc2modm(b, M) * count) % M
        return total % M
