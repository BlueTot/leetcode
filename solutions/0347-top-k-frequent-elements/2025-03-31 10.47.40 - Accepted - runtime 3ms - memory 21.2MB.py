from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = [(v,k) for k, v in Counter(nums).items()]
        counter.sort(reverse=True)
        return [item[1] for item in counter[:k]]