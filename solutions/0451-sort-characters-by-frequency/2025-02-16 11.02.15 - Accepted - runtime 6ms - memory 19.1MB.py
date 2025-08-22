from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(list(s))
        chars = sorted(((v, k) for k, v in counter.items()), reverse=True)
        return "".join(map(lambda x : x[1] * x[0], chars))