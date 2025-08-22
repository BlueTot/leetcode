import re
class Solution:
    def isNumber(self, s: str) -> bool:
        if re.match(r"^[+|-]?(((\d+|\d+\.\d*|\d*\.\d+)[e|E][+|-]?\d+)|(\d+|\d+\.\d*|\d*\.\d+))$", s):
            return True
        return False