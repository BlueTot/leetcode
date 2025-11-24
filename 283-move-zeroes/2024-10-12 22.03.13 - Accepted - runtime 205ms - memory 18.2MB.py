class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        num_nonzeroes = 0
        while i < len(nums):
            if (n := nums[i]) != 0:
                nums.pop(i)
                nums.insert(num_nonzeroes, n)
                num_nonzeroes += 1
            i += 1
        """
        Do not return anything, modify nums in-place instead.
        """
        