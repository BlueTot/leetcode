class Solution:
    def countBits(self, n: int) -> List[int]:
        num_ones = [0]*(n+1)
        for i in range(1, n+1):
            num_ones[i] = num_ones[i//2] + i % 2
        return num_ones
        