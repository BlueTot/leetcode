class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        elif n == 2:
            return [0, 1, 3, 2]
        prev = self.grayCode(n-1)
        output = prev + list(map(lambda x : x | (1 << (n-1)), prev[::-1]))
        return output