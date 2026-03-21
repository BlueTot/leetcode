class MyQueue:


    def __init__(self):
        self.__s1 = []
        self.__s2 = []
        

    def push(self, x: int) -> None:
        self.__s1.append(x)
        

    def pop(self) -> int:
        while (len(self.__s1) > 1):
            self.__s2.append(self.__s1.pop())
        res = self.__s1.pop()
        while (len(self.__s2) > 0):
            self.__s1.append(self.__s2.pop())
        return res
        

    def peek(self) -> int:
        return self.__s1[0]
        

    def empty(self) -> bool:
        return len(self.__s1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()