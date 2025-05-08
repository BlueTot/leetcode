import re

class Solution:

    def precedence(self, c):
        if c == "#":
            return 0
        elif (c in "+-"):
            return 1
        else:
            return 2

    def calculate(self, s: str) -> int:

        operands = []
        operators = []

        s += "#"

        while s:

            if s[0] == " ":
                s = s[1:]
                continue
            pattern_match = re.match(r"^(\d+)", s)
            if (pattern_match):
                operands.append(int(n := pattern_match.group(1)))
                s = s[len(n):]
            else:
                op = s[0]
                while (operators and self.precedence(operators[-1]) >= self.precedence(op)):
                    val2 = operands.pop()
                    val1 = operands.pop()
                    prevop = operators.pop()
                    if prevop == "+":
                        operands.append(val1+val2)
                    elif prevop == "-":
                        operands.append(val1-val2)
                    elif prevop == "*":
                        operands.append(val1*val2)
                    else:
                        operands.append(val1//val2)
                operators.append(op)
                s = s[1:]
            
            print(operands, operators)
        
        return operands[0]