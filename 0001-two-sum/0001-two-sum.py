class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {num : i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if target - num in indices and (j := indices[target - num]) != i:
                return [i, j]