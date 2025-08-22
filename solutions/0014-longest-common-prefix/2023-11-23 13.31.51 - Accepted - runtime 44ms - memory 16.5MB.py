class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        idx = 0
        while True:
            prefix = None
            for s in strs:
                if idx > len(s):
                    return longest_prefix
                if prefix is None: prefix = s[:idx]
                elif s[:idx] != prefix: return longest_prefix
            longest_prefix = prefix
            idx += 1

            