class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        output = []
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            rest = nums[:i] + nums[i+1:] # skip the current element
            for p in self.permuteUnique(rest):
                output.append([nums[i], *p])
            seen.add(nums[i])
        return output
