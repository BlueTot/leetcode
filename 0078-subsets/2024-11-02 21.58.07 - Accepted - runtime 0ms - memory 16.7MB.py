class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        for i in range(0, 2**len(nums)):
            power_set.append([])
            for j in range(len(nums)):
                if i % ((n := 2**j) * 2) >= n:
                    power_set[-1].append(nums[j])
        return power_set