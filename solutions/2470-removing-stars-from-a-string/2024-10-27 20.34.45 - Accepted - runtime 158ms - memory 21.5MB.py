class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        stack = []
        for i in range(len(s)):
            if s[i] == "*":
                s[i] = ""
                s[stack.pop()] = ""
            else:
                stack.append(i)
        return "".join(s)
        