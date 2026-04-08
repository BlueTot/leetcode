class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:

        M = 10**9 + 7
        
        for l, r, k, v in queries:
            for idx in range(l, r+1, k):
                nums[idx] = (nums[idx] * v) % M
        
        res = 0
        for num in nums:
            res = res ^ num

        return res
