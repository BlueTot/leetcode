class BrowserHistory:

    def __init__(self, homepage: str):
        self.__history = [homepage]
        self.__cursor = 0
        self.__tail = 0
        

    def visit(self, url: str) -> None:
        if self.__cursor == len(self.__history) - 1:
            self.__history.append(url)
            self.__cursor += 1
            self.__tail = self.__cursor
        else:
            self.__cursor += 1
            self.__tail = self.__cursor
            self.__history[self.__cursor] = url
        

    def back(self, steps: int) -> str:
        self.__cursor = max(self.__cursor - steps, 0)
        return self.__history[self.__cursor]
        

    def forward(self, steps: int) -> str:
        self.__cursor = min(self.__cursor + steps, self.__tail)
        return self.__history[self.__cursor]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)