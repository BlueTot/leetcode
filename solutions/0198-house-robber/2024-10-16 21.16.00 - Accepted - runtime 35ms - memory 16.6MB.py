from functools import lru_cache

class Solution:

    def rob(self, nums: List[int]) -> int:
        amounts = [[0, 0]]*(len(nums)+2)
        for i, num in enumerate(nums[::-1]):
            amounts[i+2] = [max(amounts[i+1]), max(*amounts[i], amounts[i+1][0]) + num]
        return max(amounts[-1])
        
        