class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        las = [0 for _ in arr]

        indices = {}
        for i, num in enumerate(arr):
            if num not in indices:
                indices[num] = set()
            indices[num].add(i)

        # indices = {v: k for k, v in enumerate(arr)}

        for i in range(len(arr)):
            longest = 0
            # for j in range(i):
            if (k := arr[i] - difference) in indices:
                for j in indices[k]:
                    longest = max(longest, las[j])
            # if (k := arr[i] - difference) in indices:
            #     longest = max(longest, las[indices[k]])
                # if arr[i] - arr[j] == difference:
                #     longest = max(longest, las[j])
                # print(i, k, las[k], longest)
            las[i] = 1 + longest
        print(las, indices)
        return max(las)