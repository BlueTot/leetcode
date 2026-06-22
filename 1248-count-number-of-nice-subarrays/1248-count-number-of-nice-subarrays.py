class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        # k = prefix[r] - prefix[l-1]
        # prefix[r] - k = prefix[l-1]

        # store number of occurrences we've seen a prefix sum before
        counts = {0: 1}
        prefix = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                prefix += 1
            if prefix - k in counts:
                res += counts[prefix - k]
            counts[prefix] = counts.get(prefix, 0) + 1

        return res
        