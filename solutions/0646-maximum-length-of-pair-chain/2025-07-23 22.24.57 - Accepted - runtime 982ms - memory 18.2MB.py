class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda p: p[1])
        lis = [0 for _ in pairs]
        for i in range(len(pairs)):
            longest = 0
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    longest = max(longest, lis[j])
            lis[i] = 1 + longest
        return max(lis)
