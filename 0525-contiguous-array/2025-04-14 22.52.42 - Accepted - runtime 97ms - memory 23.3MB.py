class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        maxLength = 0
        currSum = 0
        prefix = {0 : -1}

        for i, num in enumerate(nums):

            # idea is we transform 0s into -1, so equal number of 0s and 1s means a sum of 0
            currSum += 1 if num == 1 else -1
            
            if currSum in prefix:
                maxLength = max(maxLength, i - prefix[currSum])
            else:
                prefix[currSum] = i
        
        return maxLength