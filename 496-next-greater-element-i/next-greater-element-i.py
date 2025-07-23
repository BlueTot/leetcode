class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = [-1 for _ in nums2]
        mstack = []
        for i in range(len(nums2)):
            while mstack and nums2[mstack[-1]] < nums2[i]:
                next_greater[mstack.pop()] = nums2[i]
            mstack.append(i)
        greater_dict = {v : next_greater[i] for i, v in enumerate(nums2)}
        return [greater_dict[v] for v in nums1]