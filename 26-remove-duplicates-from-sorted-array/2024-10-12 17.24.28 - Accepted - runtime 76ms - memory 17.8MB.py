class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        i = 0
        while i < len(nums):
            if nums[i] not in s:
                s.add(nums[i])
                n = nums.pop(i)
                nums.insert(len(s)-1, n)
            i += 1
        return len(s)