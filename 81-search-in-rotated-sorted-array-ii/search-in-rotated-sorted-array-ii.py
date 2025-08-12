class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        # worst case time complexity is O(n)
        # consider array [10, 1, 10, 10, 10, 10]
        # same as a linear search here
        return target in nums
