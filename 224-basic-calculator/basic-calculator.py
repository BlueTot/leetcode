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
        last = 0

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
                last = 0
                while operators and operators[-1] == "~":
                    operands.append(-1 * operands.pop())
                    operators.pop()
            elif s[i] == "(":
                operators.append(s[i])
                i += 1
                last = 1
            elif s[i] == ")":
                while (operators and operators[-1] != "("):
                    if operators[-1] == "~":
                        operands.append(-1 * operands.pop())
                        operators.pop()
                    else:
                        operands.append(self.apply_op(operators.pop(), operands.pop(), operands.pop()))
                operators.pop()
                i += 1
                last = 0
            elif s[i] in "*+/" or s[i] == "-" and i != 0 and last == 0:
                while (operators and operators[-1] != "("):
                    if operators[-1] == "~":
                        operands.append(-1 * operands.pop())
                        operators.pop()
                    elif precedence[operators[-1]] >= precedence[s[i]]:
                        operands.append(self.apply_op(operators.pop(), operands.pop(), operands.pop()))
                    else:
                        break
                operators.append(s[i])
                i += 1
                last = 0
            else: # unary minus
                while (operators and operators[-1] == "~" and operands):
                    operands.append(-1 * operands.pop())
                operators.append("~")
                i += 1
                last = 0
            # print(operands, operators)
        
        while (operators):
            if operators[-1] == "~":
                operands.append(-1 * operands.pop())
                operators.pop()
            else:
                operands.append(self.apply_op(operators.pop(), operands.pop(), operands.pop()))
        
        return operands[0]

