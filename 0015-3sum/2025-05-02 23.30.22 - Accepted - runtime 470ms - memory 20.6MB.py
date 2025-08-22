class Solution:

    def twoSum(self, start, nums, target):
        left = start + 1
        right = len(nums)-1
        pairs = []
        while (left < right):
            total = nums[left] + nums[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else: 
                pairs.append([nums[left], nums[right]])
                while (left < right and nums[left+1] == nums[left]):
                    left += 1
                left += 1
                while (left < right and nums[right-1] == nums[right]):
                    right -= 1
                right -= 1
        return pairs
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pairs = self.twoSum(i, nums, -nums[i])
            for pair in pairs:
                lst = [nums[i]] + pair
                output.append(lst)
        return output
                
            