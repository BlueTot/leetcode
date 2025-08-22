class Solution:

    def canJump(self, nums: List[int]) -> bool:
        canJumpTo = [False for _ in range(len(nums))]
        canJumpTo[0] = True
        for index in range(len(nums)):
            if canJumpTo[len(nums)-1]:
                return True
            if canJumpTo[index]:
                for jumpAmount in range(1, nums[index]+1):
                    if index+jumpAmount < len(nums):
                        canJumpTo[index+jumpAmount] = True
        return canJumpTo[len(nums)-1]
                    