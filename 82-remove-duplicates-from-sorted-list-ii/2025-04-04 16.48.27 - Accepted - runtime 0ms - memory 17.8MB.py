# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = ListNode(None)
        output = prev
        prev.next = head
        curr = head
        while curr is not None:
            flag = False
            while (curr.next is not None and curr.next.val == curr.val):
                flag = True
                curr.next = curr.next.next
            if flag:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        
        return output.next
