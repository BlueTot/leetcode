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
