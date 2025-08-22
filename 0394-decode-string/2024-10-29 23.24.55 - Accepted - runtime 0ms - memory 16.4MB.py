class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            char = s[i]
            if char == "[":
                stack.append("")
                i += 1
            elif char == "]":
                repeated = stack[-1] * stack[-2]
                if len(stack) > 2:
                    print(stack)
                    stack[-3] += repeated
                    stack.pop()
                    stack.pop()
                else:
                    stack.pop()
                    stack.pop()
                    stack.append(repeated)
                i += 1
            elif char.isdigit():
                curr = char
                i += 1
                while i < len(s) and s[i].isdigit():
                    curr += s[i]
                    i += 1
                stack.append(int(curr))
            else:
                if not stack:
                    stack.append("")
                stack[-1] += char
                i += 1
        return stack[0]
        