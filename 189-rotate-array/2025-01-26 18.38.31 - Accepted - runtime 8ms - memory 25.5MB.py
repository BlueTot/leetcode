class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        array = [0 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            array[(i+k)%len(nums)] = num
        for i, num in enumerate(array):
            nums[i] = num
        """
        Do not return anything, modify nums in-place instead.
        """
        