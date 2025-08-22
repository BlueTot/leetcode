class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1+nums2)
        return arr[(len(arr)+1)//2-1] if len(arr) % 2 == 1 else (arr[len(arr)//2-1] + arr[len(arr)//2])/2
        