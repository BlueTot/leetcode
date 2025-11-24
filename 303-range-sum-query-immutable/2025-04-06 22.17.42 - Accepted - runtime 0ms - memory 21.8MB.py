class NumArray:

    def __init__(self, nums: List[int]):
        self.__nums = nums
        self.__prefix = []
        prefixSum = 0
        for num in nums:
            prefixSum += num
            self.__prefix.append(prefixSum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.__prefix[right]
        return self.__prefix[right] - self.__prefix[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)