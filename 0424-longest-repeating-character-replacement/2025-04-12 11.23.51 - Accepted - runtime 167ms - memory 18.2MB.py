class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        length = 0
        freq = {}

        for right in range(len(s)):

            freq[s[right]] = freq.get(s[right], 0) + 1

            while ((currLength := right - left + 1) - max(freq.values()) > k and left < right):
                freq[s[left]] -= 1
                left += 1

            length = max(length, currLength)
        
        return length
