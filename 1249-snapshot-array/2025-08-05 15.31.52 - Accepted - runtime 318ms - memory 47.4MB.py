class SnapshotArray:

    def __init__(self, length: int):
        self.__snapid = 0
        self.__arr = [[(self.__snapid, 0)] for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        if self.__arr[index][-1][0] == self.__snapid:
            self.__arr[index][-1] = (self.__snapid, val)
        else:
            self.__arr[index].append((self.__snapid, val))


    def snap(self) -> int:
        self.__snapid += 1
        return self.__snapid - 1
        

    def get(self, index: int, snap_id: int) -> int:
        arr = self.__arr[index]
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid == len(arr)-1 and arr[mid][0] <= snap_id:
                return arr[mid][1]
            elif mid > 0 and arr[mid][0] <= snap_id and arr[mid+1][0] > snap_id:
                return arr[mid][1]
            elif arr[mid][0] > snap_id:
                right = mid - 1
            else:
                left = mid + 1
        return arr[0][1]        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)