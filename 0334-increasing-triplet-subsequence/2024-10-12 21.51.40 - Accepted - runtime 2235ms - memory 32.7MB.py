from collections import deque

class Solution:

    def traverse(self, nums, i, path=[]):

        if len(path) == 3:
            return True
        
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                if self.traverse(nums, j, path+[j]):
                    return True
        
        return False

    def increasingTriplet(self, nums: List[int]) -> bool:

        if len(set(nums)) < 3:
            return False
        for i in range(len(nums)):
            if self.traverse(nums, i, [i]):
                return True
        return False
        