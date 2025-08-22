class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        running = 0
        for num in nums:
            running ^= num
        return running