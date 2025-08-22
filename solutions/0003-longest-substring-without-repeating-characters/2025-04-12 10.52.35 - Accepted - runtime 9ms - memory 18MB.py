class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        left = 0
        length = 0
    
        for right in range(len(s)):

            # if property is broken, we try to fix it by pushing left pointer
            while (s[right] in seen):
                seen.remove(s[left])
                left += 1
            
            # add right pointer, and update length
            seen.add(s[right])
            length = max(length, right - left + 1)
        
        return length
