class Solution:

    MOD = 10**9 + 7

    def numOfSubarrays(self, arr: List[int]) -> int:

        count = 0
        counter = [1, 0]
        mod = 0

        for num in arr:
            mod = (mod + num) % 2
            count += counter[mod-1]
            counter[mod] += 1
        
        return count % Solution.MOD