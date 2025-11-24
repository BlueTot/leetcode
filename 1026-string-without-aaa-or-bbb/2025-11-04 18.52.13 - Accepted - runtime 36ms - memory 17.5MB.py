class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:

        result = ""

        while a != b and a > 0 and b > 0:
            if a > b:
                result += "aab"
                a -= 2
                b -= 1
            else:
                result += "bba"
                b -= 2
                a -= 1
        print(a, b)
        if a == b:
            for i in range(a):
                result += "ab"
        elif b == 0:
            result += "a"*a
        else:
            result += "b"*b
        return result
                
                
        