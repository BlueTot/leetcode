from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mx, mxval = -1, -1
        for num, val in Counter(nums).items():
            if val > mxval:
                mx = num
                mxval = val
        return mx