class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = 0
        counter = {}
        counter[0] = 1
        for num in nums:
            prefixSum += num
            if prefixSum - k in counter:
                count += counter[prefixSum -k]
            if prefixSum in counter:
                counter[prefixSum] += 1
            else:
                counter[prefixSum] = 1
    
        return count
    