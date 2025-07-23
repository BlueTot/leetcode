class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        i = 0
        mstack = []
        result = [-1 for _ in nums]

        for _ in range(2):
            for i in range(len(nums)):
                while mstack and nums[mstack[-1]] < nums[i]:
                    j = mstack.pop()
                    if result[j] == -1:
                        result[j] = nums[i]
                if result[i] == -1:
                    mstack.append(i)

        return result
                