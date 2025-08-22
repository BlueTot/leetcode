class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        left = []
        total = 0
        for num in nums:
            total += num
            left.append(total)

        count = 0
        for i in range(0, len(nums)-1):
            if left[i] >= total - left[i]:
                count += 1
        return count