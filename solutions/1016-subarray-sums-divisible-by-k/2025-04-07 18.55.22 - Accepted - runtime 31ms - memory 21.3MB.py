class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # before processing, we know that the initial prefix sum is 0, so there is an index with the prefixSum % k being 0, so we initialise it to 1.
        counter = {0 : 1}
        mod = 0
        count = 0
        for i, num in enumerate(nums):
            mod = (mod + num) % k
            # recall that prefix[r] = prefix[l-1] (mod k) for a subarray sum divisible by k.
            # so if we have n indices before (they dont overlap) that have the same modulo, there are n subarrays that have a sum divisible by k.
            count += counter.get(mod, 0)
            # we update. the counter stores the number of incides for each given modulo
            counter[mod] = counter.get(mod, 0) + 1
        return count