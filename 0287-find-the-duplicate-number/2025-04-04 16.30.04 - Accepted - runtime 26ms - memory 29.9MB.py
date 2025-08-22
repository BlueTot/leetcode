class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if (slow == fast): break
        
        newSlow = 0
        while (slow != newSlow):
            slow = nums[slow]
            newSlow = nums[newSlow]
        
        return slow