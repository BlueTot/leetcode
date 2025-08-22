class Solution:
    def isHappy(self, n: int) -> bool:
        curr = n
        seen = set([n])
        while (curr != 1):
            curr = sum((d := int(digit))*d for digit in str(curr))
            if curr in seen:
                return False
            seen.add(curr)
        return True
        