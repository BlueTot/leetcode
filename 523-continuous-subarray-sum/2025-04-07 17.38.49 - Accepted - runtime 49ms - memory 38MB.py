class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod = 0
        array = {0 : -1} # prefix sum is 0 at index -1, base case
        for i, num in enumerate(nums):
            # we keep track of prefix sum mod k
            mod = (mod + num) % k
            # difference is 2 or more (notice that sum(l,r) = prefix[r]-prefix[l-1] so lower bound is not included)
            if mod in array:
                if i - array[mod] >= 2:
                    return True
            else: # otherwise, we store the value and move on
                array[mod] = i
        return False