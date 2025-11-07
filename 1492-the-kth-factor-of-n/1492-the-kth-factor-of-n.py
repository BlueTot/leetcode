class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        count = 0
        for f in range(1, n+1):
            if n % f == 0:
                count += 1
            if count == k:
                return f
        
        return -1
        