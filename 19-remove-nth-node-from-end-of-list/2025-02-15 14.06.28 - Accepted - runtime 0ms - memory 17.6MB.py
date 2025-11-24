# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # find length
        length = 0
        curr = head
        while (curr != None):
            curr = curr.next
            length += 1
        
        stop = length - n
        count = 0
        curr = head

        if stop == 0:
            return curr.next

        while count < stop-1:
            curr = curr.next
            count += 1

        curr.next = curr.next.next
        return head
        