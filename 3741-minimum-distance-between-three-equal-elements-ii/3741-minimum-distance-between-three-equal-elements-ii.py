class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        counter = {}
        for i in range(len(nums)):
            if nums[i] not in counter:
                counter[nums[i]] = []
            counter[nums[i]].append(i)
        
        res = float("inf")
        for indices in counter.values():
            for idx in range(max(0, len(indices) - 2)):
                i, j, k = indices[idx], indices[idx+1], indices[idx+2]
                res = min(res, abs(i-j) + abs(j-k) + abs(k-i))
    
        return -1 if res == float("inf") else res
        