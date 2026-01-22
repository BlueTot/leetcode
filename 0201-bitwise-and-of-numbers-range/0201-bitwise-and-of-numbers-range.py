class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        # next upper bound is
        # 2**(i+1)-1. if right > upper bound then we have a switch.
        # so value is 0
        # if contained it is a 1

        res = 0

        for i in range(32):
            
            # we only care about cases where left[i] is 1
            if (left & (1 << i)) == 0:
                continue

            # we compute the largest upper bound for which
            # the bit is the same
            # if right exceeds this bit then the AND will be 0
            # otherwise it will remain 1

            suffix = (1 << i) - 1
            next_upper = left & (~suffix) | suffix

            # set the bit
            if right <= next_upper:
                res |= (1 << i)
        
        return res

