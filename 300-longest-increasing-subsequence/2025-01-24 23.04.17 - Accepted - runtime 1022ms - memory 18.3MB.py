class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                longest[i] = 1
            else:
                poss = [longest[j] for j in range(i) if nums[i] > nums[j]]
                if poss:
                    longest[i] = 1 + max(poss)
        return max(longest)