# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        nums = []
        curr = head
        while curr != None:
            nums.append(curr.val)
            curr = curr.next

        mstack = []
        answer = [0 for _ in nums]
        for i in range(len(nums)):
            while mstack and nums[mstack[-1]] < nums[i]:
                answer[mstack.pop()] = nums[i]
            mstack.append(i)
        return answer