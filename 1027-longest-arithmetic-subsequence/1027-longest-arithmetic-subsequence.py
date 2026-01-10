from functools import cache

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        dp = [{} for i in range(0, len(nums))]
        res = 0
        for i in range(0, len(nums)):
            for j in range(0, i):
                dp[i][nums[i] - nums[j]] = 1 + dp[j].get(nums[i] - nums[j], 1)
            for v in dp[i].values():
                res = max(res, v)
        
        return res
        
        # @cache
        # def dp(i: int, diff: int) -> int:
        #     if i == 0:
        #         return 1
        #     res = 1
        #     for j in range(0, i):
        #         if nums[i] - nums[j] == diff:
        #             res = max(res, 1 + dp(j, diff))
        #     return res
        
        # res = 0
        # for i in range(0, len(nums)):
        #     for j in range(0, i):
        #         res = max(res, dp(i, nums[i] - nums[j]))
        
        # return res


