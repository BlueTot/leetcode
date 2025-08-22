from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eating_speed(k):
            return sum(ceil(amount / k) for amount in piles)
        
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if eating_speed(mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left