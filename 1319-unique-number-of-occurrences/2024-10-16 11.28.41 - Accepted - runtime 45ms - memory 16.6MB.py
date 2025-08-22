class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        return len(counts.values()) == len(set(counts.values()))