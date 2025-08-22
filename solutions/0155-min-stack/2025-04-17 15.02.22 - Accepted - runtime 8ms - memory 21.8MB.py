class MinStack:

    def __init__(self):
        self.__stack = []
        

    def push(self, val: int) -> None:
        if (not self.__stack):
            self.__stack.append((val, val))
        else:
            self.__stack.append((val, min(val, self.__stack[-1][1])))
        

    def pop(self) -> None:
        self.__stack.pop()
        

    def top(self) -> int:
        return self.__stack[-1][0]
        

    def getMin(self) -> int:
        return self.__stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()