class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort()
        for spell_strength in spells:
            left = 0
            right = len(potions)
            while left < right:
                mid = (left + right) // 2
                if spell_strength * potions[mid] >= success:
                    right = mid
                else:
                    left = mid + 1
            result.append(len(potions) - left)
        return result