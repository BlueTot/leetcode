# class Solution:

#     def apply_op(self, op, b, a):
#         if op == "+":
#             return a+b
#         elif op == "-":
#             return a-b
#         elif op == "*":
#             return a*b
#         elif op == "/":
#             return a//b

#     def calculate(self, s: str) -> int:
        
#         precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
#         operands = []
#         operators = []

#         i = 0
#         last = 0

#         while i < len(s):

#             if s[i] == " ":
#                 i += 1
#                 continue
#             if s[i].isdigit():
#                 num = 0
#                 while i < len(s) and s[i].isdigit():
#                     num = num * 10 + int(s[i])
#                     i += 1
#                 operands.append(num)
#                 last = 0
#                 while operators and operators[-1] == "~":
#                     operands.append(-1 * operands.pop())
#                     operators.pop()
#             elif s[i] == "(":
#                 operators.append(s[i])
#                 i += 1
#                 last = 1
#             elif s[i] == ")":
#                 while (operators and operators[-1] != "("):
#                     if operators[-1] == "~":
#                         operands.append(-1 * operands.pop())
#                         operators.pop()
#                     else:
#                         operands.append(self.apply_op(operators.pop(), operands.pop(), operands.pop()))
#                 operators.pop()
#                 i += 1
#                 last = 0
#             elif s[i] in "*+/" or s[i] == "-" and i != 0 and last == 0:
#                 while (operators and operators[-1] != "("):
#                     if operators[-1] == "~":
#                         operands.append(-1 * operands.pop())
#                         operators.pop()
#                     elif precedence[operators[-1]] >= precedence[s[i]]:
#                         operands.append(self.apply_op(operators.pop(), operands.pop(), operands.pop()))
#                     else:
#                         break
#                 operators.append(s[i])
#                 i += 1
#                 last = 0
#             else: # unary minus
#                 while (operators and operators[-1] == "~" and operands):
#                     operands.append(-1 * operands.pop())
#                 operators.append("~")
#                 i += 1
#                 last = 0
#             # print(operands, operators)
        
#         while (operators):
#             if operators[-1] == "~":
#                 operands.append(-1 * operands.pop())
#                 operators.pop()
#             else:
#                 operands.append(self.apply_op(operators.pop(), operands.pop(), operands.pop()))
        
#         return operands[0]

class Solution:
    def apply_op(self, op, b, a):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a // b

    def calculate(self, s: str) -> int:
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
        operands, operators = [], []

        def apply_top_operator():
            op = operators.pop()
            if op == "~":
                operands.append(-operands.pop())
            else:
                b, a = operands.pop(), operands.pop()
                operands.append(self.apply_op(op, b, a))

        i, n = 0, len(s)
        expect_operand = True

        while i < n:
            ch = s[i]

            if ch == " ":
                i += 1
                continue

            if ch.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                operands.append(num)
                expect_operand = False
                while operators and operators[-1] == "~":
                    apply_top_operator()

            elif ch == "(":
                operators.append(ch)
                i += 1
                expect_operand = True

            elif ch == ")":
                while operators and operators[-1] != "(":
                    apply_top_operator()
                operators.pop()  # pop "("
                i += 1
                expect_operand = False

                # FIX: Apply unary minus after closing parenthesis
                while operators and operators[-1] == "~":
                    apply_top_operator()

            elif ch in "+-*/":
                if ch == "-" and expect_operand:
                    operators.append("~")
                else:
                    while (operators and operators[-1] != "(" and
                           operators[-1] != "~" and
                           precedence[operators[-1]] >= precedence[ch]):
                        apply_top_operator()
                    operators.append(ch)
                    expect_operand = True
                i += 1

        while operators:
            apply_top_operator()

        return operands[0]
