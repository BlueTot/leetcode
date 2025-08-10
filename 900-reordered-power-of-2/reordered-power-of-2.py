from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for i in range(30):
            power = 1 << i
            if Counter(str(power)) == Counter(str(n)):
                return True
        return False