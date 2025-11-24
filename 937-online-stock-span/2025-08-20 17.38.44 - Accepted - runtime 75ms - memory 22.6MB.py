class StockSpanner:

    def __init__(self):
        self.__i = 0
        self.__mstack: List[Tuple[int, int]] = []
        

    def next(self, price: int) -> int:
        while self.__mstack and self.__mstack[-1][0] <= price:
            self.__mstack.pop()
        result = self.__i - (self.__mstack[-1][1] if self.__mstack else -1)
        self.__mstack.append((price, self.__i))
        self.__i += 1
        return result
        
             


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)