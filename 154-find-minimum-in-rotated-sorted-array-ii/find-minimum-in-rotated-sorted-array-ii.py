class Solution:
    def findMin(self, nums: List[int]) -> int:

        # it is not possible to use O(log n) time to find the solution
        # e.g. [10, 1, 10, 10, 10]
        # if you take mid = 2, then you would move right but cannot find it.
        # if the 1 was on the other side, you would find it
        # in the worst case this is equivalent to finding the index that satisfies a predicate where the index only occurs once, i.e. a linear search.
        return min(nums)
        