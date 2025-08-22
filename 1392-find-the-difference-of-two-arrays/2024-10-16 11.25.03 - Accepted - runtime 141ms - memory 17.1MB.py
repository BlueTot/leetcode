class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        answer = [sorted(s1 - s2), sorted(s2 - s1)]
        return answer