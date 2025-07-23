class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        las = [0 for _ in arr]

        indices = {}
        for i, num in enumerate(arr):
            if num not in indices:
                indices[num] = set()
            indices[num].add(i)

        for i in range(len(arr)):
            longest = 0
            if (k := arr[i] - difference) in indices:
                for j in indices[k]:
                    longest = max(longest, las[j])
            las[i] = 1 + longest
        print(las, indices)
        return max(las)