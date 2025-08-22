from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(a, b):
            if int(f"{a}{b}") > int(f"{b}{a}"):
                return 1
            return -1
        
        nums.sort(key = cmp_to_key(compare), reverse=True)
        if (s := "".join(map(str, nums)))[0] == '0':
            return "0"
        return s