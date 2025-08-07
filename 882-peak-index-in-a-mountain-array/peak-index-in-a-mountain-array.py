class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        while left < right:
            mid = (left + right) // 2
            if mid == len(arr)-1 or arr[mid] > arr[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left