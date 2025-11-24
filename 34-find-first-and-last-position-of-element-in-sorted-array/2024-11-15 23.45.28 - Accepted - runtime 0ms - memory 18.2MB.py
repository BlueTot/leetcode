class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        lower, upper = 0, len(nums) - 1
        while True:
            if nums[lower] == target:
                upper = lower
                break
            elif nums[upper] == target:
                lower = upper
                break
            if lower == upper:
                return [-1, -1]
            mid = (lower + upper) // 2
            if lower == mid:
                lower += 1
            elif target < nums[mid]:
                upper = mid
            elif target > nums[mid]:
                lower = mid
            else:
                lower = mid
                upper = mid
                break
        while lower > 0:
            if nums[lower-1] != target:
               break
            lower -= 1
        while upper < len(nums) - 1:
            if nums[upper+1] != target:
                break
            upper += 1
        return [lower, upper]
            