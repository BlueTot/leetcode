class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char in "+-*/":
                arg2 = stack.pop()
                arg1 = stack.pop()
                if char == "+":
                    stack.append(arg1+arg2)
                elif char == "-":
                    stack.append(arg1-arg2)
                elif char == "*":
                    stack.append(arg1*arg2)
                else:
                    stack.append(int(arg1/arg2))
            else:
                stack.append(int(char))
        return stack[0]