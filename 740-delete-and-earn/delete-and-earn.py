from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = sorted([(k, v) for k, v in Counter(nums).items()])
        scores = [0 for _ in counts]
        for i, item in enumerate(counts):
            num, count = item
            if i >= 2 and counts[i-1][0] == num - 1:
                scores[i] = max(num * count, num * count + scores[i-2], scores[i-1])
            elif i >= 1 and counts[i-1][0] < num - 1:
                scores[i] = num * count + scores[i-1]
            elif i >= 1:
                scores[i] = max(num * count, scores[i-1])
            else:
                scores[i] = num * count
        return max(scores)
            