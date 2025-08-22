# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import floor
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        n = 0
        while curr.next is not None:
            curr = curr.next
            n += 1
        if n == 0:
            return None
        curr = head
        for _ in range(n//2 if n % 2 == 1 else n//2 - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head

        