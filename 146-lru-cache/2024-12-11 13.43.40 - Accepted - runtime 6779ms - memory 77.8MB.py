class LRUCache:

    def __init__(self, capacity: int):
        self.__usedCounter = 0
        self.__dict = {}
        self.__capacity = capacity

    def get(self, key: int) -> int:
        if key in self.__dict:
            self.__dict[key][1] = self.__usedCounter
            self.__usedCounter += 1
            return self.__dict[key][0]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key not in self.__dict and len(self.__dict) == self.__capacity:
            minKey = min(self.__dict, key=lambda k : self.__dict[k][1])
            self.__dict.pop(minKey)
        self.__dict[key] = [value, self.__usedCounter]
        self.__usedCounter += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)