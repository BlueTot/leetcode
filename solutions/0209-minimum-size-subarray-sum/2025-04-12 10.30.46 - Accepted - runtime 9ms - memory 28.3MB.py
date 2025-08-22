class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        length = float("inf")
        total = 0
        
        for right in range(len(nums)):
            total += nums[right]

            while (total >= target and left < right):
                length = min(length, right - left + 1)
                total -= nums[left]
                left += 1
            
            if total >= target:
                length = min(length, right - left + 1)
        
        return length if length != float("inf") else 0
