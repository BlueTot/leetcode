class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [0]*k
        self.front = 0
        self.rear = -1
        self.length = 0
        self.k = k
        

    def enQueue(self, value: int) -> bool:
        if (self.length == self.k):
            return False
        self.rear = (self.rear + 1)% self.k
        self.arr[self.rear] = value
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if (self.length == 0):
            return False
        self.front = (self.front + 1) % self.k
        self.length -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.rear]
        

    def isEmpty(self) -> bool:
        return self.length == 0
        

    def isFull(self) -> bool:
        return self.length == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()