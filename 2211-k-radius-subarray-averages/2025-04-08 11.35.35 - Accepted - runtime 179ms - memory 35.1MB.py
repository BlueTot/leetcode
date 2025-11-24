class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        prefix = []
        prefixSum = 0
        for num in nums:
            prefixSum += num
            prefix.append(prefixSum)
        
        averages = []
        for i in range(len(nums)):
            if i - k >= 0 and i + k < len(nums):
                upper = prefix[i+k]
                lower = prefix[i-k-1] if i-k-1 >= 0 else 0
                averages.append((upper - lower) // (2*k + 1))
            else:
                averages.append(-1)
        return averages