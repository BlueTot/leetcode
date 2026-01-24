class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        res = 0

        for i in range(0, len(nums) // 2):
            res = max(res, nums[i] + nums[len(nums)-1-i])
        
        return res