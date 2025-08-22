class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        lengths = [0, 0]
        maximum = 0
        has0 = False
        num_shuffles = 0
        for i in range(len(nums)):
            if i == 0 and nums[i] == 1 or nums[i-1] == 0 and i > 0:
                lengths[1] = lengths[0]
                lengths[0] = 0
                num_shuffles += 1
            if nums[i] == 1:
                lengths[0] += 1
            if nums[i] == 0:
                has0 = True
            maximum = max(maximum, lengths[0]+lengths[1])
        if num_shuffles == 0 and has0:
            return lengths[0]
        if not has0:
            return lengths[0]-1
        return maximum



                
        