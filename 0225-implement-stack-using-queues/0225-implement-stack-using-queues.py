from collections import deque

class MyStack:

    def __init__(self):
        self.__q1 = deque()
        self.__q2 = deque()
        

    def push(self, x: int) -> None:
        self.__q1.append(x)

    def pop(self) -> int:
        while len(self.__q1) > 1:
            self.__q2.append(self.__q1.popleft())
        res = self.__q1.popleft()
        while len(self.__q2) > 0:
            self.__q1.append(self.__q2.popleft())
        return res
        

    def top(self) -> int:
        return self.__q1[-1]
        

    def empty(self) -> bool:
        return len(self.__q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()