from collections import Counter
from heapq import heappop, heappush
from functools import cmp_to_key

class Pair:
    def __init__(self, val, count):
        self.val = val
        self.count = count
    
    def __lt__(self, pair) -> bool:
        if self.count != pair.count:
            return self.count < pair.count
        return self.val > pair.val


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        pq = []
        for i, pair in enumerate(Counter(words).items()):
            if i < k:
                heappush(pq, Pair(*pair))
            else:
                heappush(pq, Pair(*pair))
                if (len(pq) > k):
                    heappop(pq)
        
        result = []
        while pq:
            result.append(heappop(pq).val)
        return result[::-1]