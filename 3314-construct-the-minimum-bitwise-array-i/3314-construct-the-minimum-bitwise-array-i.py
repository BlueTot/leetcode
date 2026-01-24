from math import log2, floor

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        res = []
        for num in nums:

            # if even, we can't split
            if num & 1 == 0:
                res.append(-1)
                continue

            # iterate through bits from MSB to LSB
            # and unset them and check if we can recompute the number
            
            for i in range(floor(log2(num)), -1, -1):
                x = num - (1 << i)
                if x | (x + 1) == num:
                    res.append(x)
                    break
        
        return res
            