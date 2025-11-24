class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set([i for i in nums if i > 0])
        if not nums or min(nums) > 1:
            return 1
        else:
            smallest = float("inf")
            for num in nums:
                if num >= 0 and num+1 not in nums:
                    smallest = min(smallest, num+1)
                if num > 1 and num-1 not in nums:
                    smallest = min(smallest, num-1)
            return smallest