class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        newArray = []
        i, j = 0, 0
        while (i < m and j < n):
            if nums1[i] <= nums2[j]:
                newArray.append(nums1[i])
                i += 1
            else:
                newArray.append(nums2[j])
                j += 1
        while (i < m):
            newArray.append(nums1[i])
            i += 1
        while (j < n):
            newArray.append(nums2[j])
            j += 1
        for i in range(m+n):
            nums1[i] = newArray[i]
        