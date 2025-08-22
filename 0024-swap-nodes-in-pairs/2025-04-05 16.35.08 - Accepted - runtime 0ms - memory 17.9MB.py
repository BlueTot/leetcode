# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while (curr != None):
            if (curr.next is not None):
                curr.val, curr.next.val = curr.next.val, curr.val
                curr = curr.next.next
            else:
                curr = curr.next
        return head