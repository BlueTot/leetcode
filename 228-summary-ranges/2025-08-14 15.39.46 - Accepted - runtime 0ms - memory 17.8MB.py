class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        if not nums:
            return []
        for i in range(len(nums)):
            if i == 0:
                start = nums[i]
            elif nums[i] > nums[i-1] + 1:
                if start == nums[i-1]:
                    output.append(f"{start}")
                else:
                    output.append(f"{start}->{nums[i-1]}")
                start = nums[i]
        if start == nums[-1]:
            output.append(f"{start}")
        else:
            output.append(f"{start}->{nums[-1]}")
        return output