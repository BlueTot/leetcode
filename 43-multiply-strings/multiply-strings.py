class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        VALS = {str(i):i for i in range(10)}

        def val(s):
            value = 0
            power = 1
            for char in reversed(s):
                value += power * VALS[char]
                power *= 10
            return value
        
        return str(val(num1) * val(num2))
