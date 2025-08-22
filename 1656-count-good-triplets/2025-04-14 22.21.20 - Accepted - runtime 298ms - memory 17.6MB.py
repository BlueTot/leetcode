class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    x, y, z = arr[i], arr[j], arr[k]
                    if abs(x - y) <= a and abs(y - z) <= b and abs(x - z) <= c:
                        count += 1
        return count