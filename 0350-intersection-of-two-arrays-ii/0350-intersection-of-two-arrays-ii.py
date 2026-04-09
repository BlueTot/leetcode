from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        counter1, counter2 = Counter(nums1), Counter(nums2)
        result = []

        for k, v in counter1.items():
            for _ in range(min(v, counter2.get(k, 0))):
                result.append(k)
        
        return result