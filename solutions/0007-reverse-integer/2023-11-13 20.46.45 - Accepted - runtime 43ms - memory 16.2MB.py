class Solution:
    def reverse(self, x: int) -> int:
        n = str(x)
        if n[0] == "-":
            lst = [i for i in n[1:]]
            lst.reverse()
            output = -int("".join(lst))
            
        else:
            lst = [i for i in n]
            lst.reverse()
            output = int("".join(lst))
        if output > 2**31 - 1 or output < -(2**31):
            return 0
        return output