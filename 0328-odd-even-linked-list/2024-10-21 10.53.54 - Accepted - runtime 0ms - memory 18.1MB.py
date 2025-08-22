# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        odd = head
        even = None
        even_head = None

        if head.next is None or head.next.next is None:
            return head

        while True:

            if odd.next is None or odd.next.next is None:
                odd.next = even_head
                break

            if even is None:
                even = odd.next
                even_head = even

            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        return head
        
    