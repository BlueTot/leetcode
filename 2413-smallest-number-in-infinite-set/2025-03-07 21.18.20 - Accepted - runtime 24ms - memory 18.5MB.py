class SmallestInfiniteSet:

    def __init__(self):
        self.__notPresent = set()
        self.__smallest = 1
        

    def popSmallest(self) -> int:
        output = self.__smallest
        self.__notPresent.add(self.__smallest)
        self.__smallest += 1
        while True:
            if (self.__smallest not in self.__notPresent):
                break
            self.__smallest += 1
        return output

    def addBack(self, num: int) -> None:
        if num in self.__notPresent:
            self.__notPresent.remove(num)
            self.__smallest = min(self.__smallest, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)