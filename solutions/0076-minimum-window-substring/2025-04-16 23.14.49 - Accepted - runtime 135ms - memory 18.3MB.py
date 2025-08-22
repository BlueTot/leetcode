from collections import Counter, defaultdict

class Solution:

    def isAtLeast(self, freq1, freq2) -> bool:
        for char, count in freq2.items():
            if freq1.get(char, 0) < count:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        
        origFreq = Counter(t)
        freq = defaultdict(int)
        length = float("inf")
        substring = ""
        left = 0
        formed = 0 # number of characters with count hit
        required = len(origFreq) # number of required characters to complete

        for right in range(len(s)):
            freq[s[right]] += 1

            if (s[right] in origFreq and freq[s[right]] == origFreq[s[right]]):
                formed += 1

            while (left <= right and formed == required):
                if (newLength := right - left + 1) < length:
                    length = newLength
                    substring = s[left:right+1]
                freq[s[left]] -= 1
                if (s[left] in origFreq and freq[s[left]] < origFreq[s[left]]):
                    formed -= 1
                left += 1

        return substring