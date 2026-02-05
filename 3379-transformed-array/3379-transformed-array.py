class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:

        res = [0]*len(nums)

        for i in range(len(nums)):
            res[i] = nums[(i + nums[i]) % len(nums)]

        return res