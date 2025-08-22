from functools import lru_cache

class Solution:

    @lru_cache
    def generate(self, n : int) -> Set[str]:
        if n == 0: return [""]
        if n == 1: return ["()"]

        output = set()
        for k in range(0, n):
            inner = self.generate(k)
            remaining = self.generate(n-k-1)
            for p1 in inner:
                for p2 in remaining:
                    output.add(f"({p1}){p2}")

        return output

    def generateParenthesis(self, n: int) -> List[str]:
        return list(self.generate(n))
        