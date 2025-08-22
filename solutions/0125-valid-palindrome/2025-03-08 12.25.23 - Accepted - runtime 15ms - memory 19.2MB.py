class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = list(
            filter((lambda c : ord('a') <= ord(c) <= ord('z') or 
                                ord('0') <= ord(c) <= ord('9')),
                    list(s.lower())))
        return lower == lower[::-1]