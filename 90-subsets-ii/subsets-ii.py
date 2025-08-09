class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        rem = self.subsetsWithDup(nums[1:])
        result = list(map(tuple, rem))
        result.extend([tuple(sorted([nums[0], *subset])) for subset in rem])
        return list(map(tuple, set(result)))
