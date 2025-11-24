from heapq import heappush, heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        # sort by the second array
        # important to sort in reverse so we can build a running top k sum
        # from the larger end downwards, which is valid
        # impossible if we sort in ascending

        nums = sorted(list(zip(nums1, nums2)), key=lambda t:t[1], reverse=True)

        largest = 0
        total = 0
        min_heap = []
        for i in range(0, len(nums)):

            # standard top k sum technique
            if i < k - 1:
                heappush(min_heap, nums[i][0])
                total += nums[i][0]
            else:
                heappush(min_heap, nums[i][0])
                total += nums[i][0]
                if (len(min_heap) > k):
                    total -= heappop(min_heap) # remove the smallest
                largest = max(largest, nums[i][1] * total)
        
        return largest

