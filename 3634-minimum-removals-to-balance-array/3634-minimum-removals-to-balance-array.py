class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left, right = 0, 0
        res = 0

        while (right < len(nums)):

            while (nums[right] / nums[left] > k and left <= right):
                left += 1

            res = max(res, right - left + 1)
            right += 1

        return len(nums) - res
            
