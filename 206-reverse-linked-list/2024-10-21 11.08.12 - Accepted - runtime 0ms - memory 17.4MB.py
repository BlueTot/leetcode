# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr, prev = head, None
        while True:
            if curr.next is None:
                curr.next = prev
                return curr
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
            