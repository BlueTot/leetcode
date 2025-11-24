class Solution:

    @staticmethod
    def f(n):
        return 2*(n-1)

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: # base case
            return s
        
        output = ""
        for row in range(numRows):
            i = row
            c = 0
            inc = 1
            while i < len(s):
                if inc != 0:
                    output += s[i]
                i += (inc := self.f(numRows - row if c % 2 == 0 else row + 1))
                c += 1

        return output     