class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complement = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in "([{": # open braces
                stack.append(char)
            elif stack and stack[-1] == complement[char]:
                stack.pop()
            else:
                return False
        return False if stack else True