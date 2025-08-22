import re

class Solution:

    def apply_op(self, op, b, a):
        if op == "+":
            return a+b
        elif op == "-":
            return a-b
        elif op == "*":
            return a*b
        elif op == "/":
            return a//b

    def calculate(self, s: str) -> int:

        precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
        operands = []
        operators = []

        i = 0

        while i < len(s):

            if s[i] == " ":
                i += 1
                continue
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                operands.append(num)
            else:
                while (operators and precedence[operators[-1]] >= precedence[s[i]]):
                    operands.append(self.apply_op(operators.pop(), operands.pop(), operands.pop()))
                operators.append(s[i])
                i += 1
        
        while (operators):
            operands.append(self.apply_op(operators.pop(), operands.pop(), operands.pop()))
        
        return operands[0]