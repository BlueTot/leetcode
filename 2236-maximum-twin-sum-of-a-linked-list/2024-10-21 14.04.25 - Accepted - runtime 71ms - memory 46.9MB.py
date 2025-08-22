# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        maximum = 0
        for i in range(len(nums)//2):
            maximum = max(maximum, nums[i] + nums[-(i+1)])
        return maximum
            
