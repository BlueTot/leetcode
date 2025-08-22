class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums) - 1
        while True:
            mid = (lower + upper) // 2
            if lower == mid:
                if lower == upper:
                    if target == nums[lower]:
                        return lower
                    return lower if target < nums[lower] else upper + 1
                if nums[lower+1] == target:
                    return lower+1
                else:
                    if nums[lower] < target and nums[upper] > target:
                        return upper
                    elif nums[lower] < target and nums[upper] < target:
                        return upper+1
                    else:
                        return lower
            elif target < nums[mid]:
                upper = mid
            elif target > nums[mid]:
                lower = mid
            else:
                return mid