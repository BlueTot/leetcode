class Solution:
    def jump(self, nums: List[int]) -> int:
        minJumps = [float("inf") for _ in range(len(nums))]
        minJumps[0] = 0
        for i in range(len(nums)):
            for k in range(1, nums[i] + 1):
                if i+k < len(nums):
                    minJumps[i+k] = min(minJumps[i+k], minJumps[i]+1)
        return minJumps[-1]
        