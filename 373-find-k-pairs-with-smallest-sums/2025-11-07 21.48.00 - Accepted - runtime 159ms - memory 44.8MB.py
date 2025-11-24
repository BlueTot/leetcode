from heapq import heappop, heappush

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        min_heap = []
        res = []

        for i in range(len(nums1)):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        while len(res) < k:
            _, i, j = heappop(min_heap)
            res.append([nums1[i], nums2[j]])
            if j < len(nums2) - 1:
                heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
        
        return res
