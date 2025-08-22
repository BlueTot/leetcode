class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(len(str1) if len(str1) < len(str2) else len(str2), -1, -1):
            prefix = str1[:i+1]
            if str2[:i+1] == prefix and len(str1)//len(prefix) * prefix == str1 and len(str2)//len(prefix) * prefix == str2:
                return prefix
        return ""
        