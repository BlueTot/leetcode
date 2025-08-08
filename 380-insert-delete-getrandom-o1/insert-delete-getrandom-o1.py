from random import choice

class RandomizedSet:

    def __init__(self):
        self.__set = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.__set:
            self.__set.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.__set:
            self.__set.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return choice(list(self.__set))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()