class Solution:

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        left = 0
        count = 0

        for right in range(len(nums)):

            while (left < right and nums[right] - nums[right-1] != nums[left+1] - nums[left]):
                left += 1
            
            count += max(0, right - left + 1 - 2)
        
        return count
