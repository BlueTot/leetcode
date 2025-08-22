class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lts = [(0, 0) for _ in nums]
        best = 0
        for i in range(len(nums)):
            if i == 0:
                lts[i] = (1, 1)
            else:
                largest = 0
                for j in range(i):
                    if nums[j] < nums[i]: 
                        largest = max(largest, lts[j][0])
                count = 0
                for j in range(i):
                    if nums[j] < nums[i] and lts[j][0] == largest:
                        count += lts[j][1]
                lts[i] = (largest + 1, max(1, count))
            best = max(best, lts[i][0])
        output = 0
        for length, count in lts:
            if length == best:
                output += count
        return output
        
