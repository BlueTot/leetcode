from math import log2

class Solution:
    def integerReplacement(self, n: int) -> int:
        
        steps = 0
        while n > 1:

            print(bin(n))

            if n & 1 == 0:
                n >>= 1
                steps += 1

            else:

                length = int(log2(n))

                pos1 = int(log2((n+1) & -(n+1)))
                length1 = int(log2(n+1))

                pos2 = int(log2((n-1) & -(n-1)))
                length2 = int(log2(n-1))
            
                print(pos1, pos2, length, length1, length2)

                if pos1 - (length1 - length) > pos2 - (length2 - length):
                    n += 1
                else:
                    n -= 1
                steps += 1

        return steps