class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = 0
        prev = None

        currStore = 0
        currLook = 0

        while (currLook < len(nums)):
            if prev != nums[currLook]:
                count = 1
            else:
                count += 1
            prev = nums[currLook]
            if count > 2:
                currLook += 1
            else:
                nums[currStore] = nums[currLook]
                currStore += 1
                currLook += 1
        
        return currStore
