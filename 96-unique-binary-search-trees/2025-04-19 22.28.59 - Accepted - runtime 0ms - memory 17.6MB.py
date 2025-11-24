class Solution:
    def numTrees(self, n: int) -> int:
        numUnique = [0]*(n+1)
        numUnique[0] = 1
        for i in range(1, n+1):
            for k in range(0, i):
                numUnique[i] += numUnique[k] * numUnique[i-k-1]
        return numUnique[n]
