class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        

        # 5 = 101
        # 6 = 110
        # 7 = 111

        
        # next upper bound is
        # 2**(i+1)-1. if right > upper bound then we have a switch.
        # so value is 0
        # if contained it is a 1

        res = 0

        for i in range(32):
            
            # we only care about cases where left[i] is 1
            if (left & (1 << i)) == 0:
                continue

            suffix = (1 << i) - 1
            next_upper = left & (~suffix) | suffix

            print(i, next_upper)
            if right <= next_upper:
                res |= (1 << i)
        
        return res

