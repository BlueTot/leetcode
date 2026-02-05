from math import log2

class Solution:
    def integerReplacement(self, n: int) -> int:
        
        steps = 0
        while n > 1:

            if n & 1 == 0:
                n >>= 1
                steps += 1

            else:
                
                # we want to see where the lowest set bit of n+1 and n-1 are
                # we choose the one with the highest lowest set bit
                # but we also must account for increasing the bit length of n
                # so we include length1-length and length2-length in the calculations

                length = int(log2(n))

                pos1 = int(log2((n+1) & -(n+1)))
                length1 = int(log2(n+1))

                pos2 = int(log2((n-1) & -(n-1)))
                length2 = int(log2(n-1))

                # choose the one giving the furthest lowest set bit and length combination
                if pos1 - (length1 - length) > pos2 - (length2 - length):
                    n += 1
                else:
                    n -= 1
                steps += 1

        return steps