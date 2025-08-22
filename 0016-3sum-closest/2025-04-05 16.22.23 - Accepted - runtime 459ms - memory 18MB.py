class Solution:

    def twoSum(self, start, nums, target):
        left = start + 1
        right = len(nums)-1
        minPair, minDist = None, float("inf")
        while (left < right):
            total = nums[left] + nums[right]
            ndist = abs(total - target)
            if total < target:
                if (ndist < minDist):
                    minPair = [nums[left], nums[right]]
                    minDist = ndist
                left += 1
            elif total > target:
                if (ndist < minDist):
                    minPair = [nums[left], nums[right]]
                    minDist = ndist
                right -= 1
            else: 
                if (ndist < minDist):
                    minPair = [nums[left], nums[right]]
                    minDist = ndist
                while (left < right - 1 and nums[left+1] == nums[left]):
                    left += 1
                left += 1
                while (right > left + 1 and nums[right-1] == nums[right]):
                    right -= 1
                right -= 1
        return minPair
        
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minSum, minDist = None, float("inf")
        for i in range(len(nums)):
            pair = self.twoSum(i, nums, target - nums[i])
            if pair is not None:
                ndist = abs(target - (nums[i] + sum(pair)))
                if ndist < minDist:
                    minSum = nums[i] + sum(pair)
                    minDist = ndist
        return minSum
        