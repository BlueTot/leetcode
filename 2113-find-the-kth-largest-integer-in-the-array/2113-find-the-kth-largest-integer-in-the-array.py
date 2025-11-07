class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        nums.sort(key = lambda s : int(s), reverse=True)
        return nums[k-1]