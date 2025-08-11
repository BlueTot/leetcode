from itertools import combinations

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        for i, num in enumerate(nums):
            if num not in indices:
                indices[num] = []
            indices[num].append(i)
        for n, indexes in indices.items():
            for i1, i2 in combinations(indexes, 2):
                if abs(i1 - i2) <= k:
                    return True
        return False