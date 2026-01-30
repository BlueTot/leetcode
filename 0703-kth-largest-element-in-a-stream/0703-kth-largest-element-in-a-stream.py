from heapq import heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.__heap = []
        self.__k = k

        for num in nums:
            if len(self.__heap) == self.__k:
                if self.__heap[0] < num:
                    heappop(self.__heap)
                    heappush(self.__heap, num)
            else:
                heappush(self.__heap, num)
        print(self.__heap)
        
    def add(self, val: int) -> int:
        if len(self.__heap) == self.__k:
            if self.__heap[0] < val:
                heappop(self.__heap)
                heappush(self.__heap, val)
        else:
            heappush(self.__heap, val)
        return self.__heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)