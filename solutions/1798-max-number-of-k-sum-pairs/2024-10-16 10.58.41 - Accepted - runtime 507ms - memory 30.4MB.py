class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        seen = set()
        total = 0
        for x, c in counts.items():
            if x not in seen:
                if k - x in counts:
                    if x == k // 2 and k % 2 == 0:
                        total += counts[x] // 2
                    else:
                        total += min(counts[x], counts[k-x])
                    seen.add(x)
                    seen.add(k-x)
        return total
            

        