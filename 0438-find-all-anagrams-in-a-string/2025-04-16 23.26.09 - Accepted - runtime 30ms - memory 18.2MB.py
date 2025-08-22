from collections import Counter

class Solution:

    def isSubset(self, freq1, freq2):

        for item in (set(freq1.keys()) | set(freq2.keys())):
            if freq1.get(item, 0) > freq2.get(item, 0):
                return False
        return True
    
    def equals(self, freq1, freq2):
        return self.isSubset(freq1, freq2) and self.isSubset(freq2, freq1)

    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        anagrams = []
        origFreq = [0]*26
        for char in p:
            origFreq[ord(char)-ord("a")] += 1
        freq = [0]*26

        for i in range(len(s)):
            if i < len(p):
                freq[ord(s[i])-ord("a")] += 1
            else:
                freq[ord(s[i])-ord("a")] += 1
                freq[ord(s[i-len(p)]) - ord("a")] -= 1
            if i >= len(p)-1 and freq == origFreq:
                anagrams.append(i-len(p)+1)
        return anagrams



        left = 0
        output = []
        freq = {}

        for right in range(len(s)):

            freq[s[right]] = freq.get(s[right], 0) + 1

            while (not self.isSubset(freq, origFreq) and left < right):
                freq[s[left]] -= 1
                left += 1     
            
            if self.equals(freq, origFreq):
                output.append(left)
        
        return output