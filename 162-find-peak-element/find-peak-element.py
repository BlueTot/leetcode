class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def get(nums, i):
            return nums[i] if 0 <= i < len(nums) else -float("inf")

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if get(nums, mid-1) < nums[mid] and get(nums, mid+1) < nums[mid]:
                return mid
            if get(nums, mid-1) < nums[mid] < get(nums, mid+1):
                left = mid + 1
            elif get(nums, mid-1) > nums[mid] > get(nums, mid+1):
                right = mid - 1
            else:
                left = mid + 1
        
            