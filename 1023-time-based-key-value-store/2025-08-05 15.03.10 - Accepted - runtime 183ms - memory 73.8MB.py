class TimeMap:

    def __init__(self):
        self.__timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.__timemap:
            self.__timemap[key] = [(timestamp, value)]
        else:
            self.__timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.__timemap:
            return ""
        arr = self.__timemap[key]
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid == len(arr)-1 and arr[mid][0] <= timestamp:
                return arr[mid][1]
            elif mid > 0 and arr[mid-1][0] <= timestamp and arr[mid][0] > timestamp:
                return arr[mid-1][1]
            elif arr[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        return ""
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)