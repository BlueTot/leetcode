class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total = 0
        past_1 = -2
        for i, char in enumerate(flowerbed):
            if char == 1:
                if i != 0:
                    total += ((i - past_1) // 2) - 1
                past_1 = i
        if flowerbed[-1] == 0:
            total += (len(flowerbed) - past_1 - 1) // 2
        return total >= n
            