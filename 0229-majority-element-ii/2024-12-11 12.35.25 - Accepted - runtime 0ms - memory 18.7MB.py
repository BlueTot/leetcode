from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [num for num, times in Counter(nums).items() if times > len(nums)//3]
