class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for substring in s.split(" ")[::-1]:
            if substring:
                return len(substring)