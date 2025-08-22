class Solution:

    def rle(self, n : str):
        prev = None
        start = None
        output = ""
        for i, char in enumerate(n):
            if prev is None:
                prev = char
                start = i
            elif char != prev:
                output += f"{i - start}{prev}"
                prev = char
                start = i
        output += f"{len(n) - start}{prev}"
        return output

    def countAndSay(self, n: int) -> str:
        curr = "1"
        if n == 1:
            return curr
        for i in range(2, n+1):
            curr = self.rle(curr)
            print(curr)
        return curr