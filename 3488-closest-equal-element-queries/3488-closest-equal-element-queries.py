class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        min_dists = [float("inf")] * len(nums)
        last_seen = {}

        for i in range(len(nums)*2):

            j = i % len(nums)
            if nums[j] in last_seen and (prev := last_seen[nums[j]]) % len(nums) != j:
                min_dists[prev % len(nums)] = min(min_dists[prev % len(nums)], abs(i - prev))
                min_dists[j] = min(min_dists[j], abs(i - prev))

            last_seen[nums[j]] = i
        
        res = []
        for index in queries:
            dist = min_dists[index]
            res.append(dist if dist != float("inf") else -1)
        
        return res