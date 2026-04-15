class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        for i in range(len(nums)):

            left = start - i
            right = start + i

            if left >= 0 and nums[left] == target:
                return i
            if right < len(nums) and nums[right] == target:
                return i
    