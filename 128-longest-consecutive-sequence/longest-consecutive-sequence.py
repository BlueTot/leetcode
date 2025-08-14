class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        length = 0
        for n in numsset:
            if n-1 in numsset:
                continue
            curr = n
            while curr + 1 in numsset:
                curr += 1
            length = max(length, curr - n + 1)
        return length
        