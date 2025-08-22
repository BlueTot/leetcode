class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for char in s:
            if char.islower():
                result.append(char)
            elif char == "*":
                if result: result.pop()
            elif char == "#":
                result.extend(result[:])
            elif char == "%":
                result = result[::-1]
        return "".join(result)