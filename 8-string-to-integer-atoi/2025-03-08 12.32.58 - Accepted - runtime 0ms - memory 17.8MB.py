import re

class Solution:
    def myAtoi(self, s: str) -> int:
        if re.match(r"^( )*[-|+]?0*\d+.*$", s):
            groups = re.findall(r"( )*([-|+]?)0*(\d+).*", s)[0]
            if groups[1] == "-":
                output = -int(groups[2])
            else:
                output = int(groups[2])
            if output > 2**31-1:
                return 2**31-1
            elif output < -(2**31):
                return -(2**31)
            else:
                return output
        return 0