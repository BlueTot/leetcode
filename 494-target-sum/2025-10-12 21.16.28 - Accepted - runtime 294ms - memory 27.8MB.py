from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def ways(nums, target) -> int:

            if len(nums) == 1:
                if target == 0:
                    return 1 + (nums[0] == 0)
                return 1 if nums[0] * 2 == target else 0
            
            return ways(tuple(list(nums)[1:]), target) + ways(tuple(list(nums)[1:]), target - nums[0] * 2)



        return ways(tuple(nums), target + sum(nums))