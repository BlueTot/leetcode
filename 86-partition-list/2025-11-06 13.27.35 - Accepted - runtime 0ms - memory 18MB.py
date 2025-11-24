# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less_than_x = []
        curr = head
        while (curr != None and curr.next != None):
            if curr.next.val < x:
                less_than_x.append(curr.next.val)
                curr.next = curr.next.next
            else:
                curr = curr.next

        less_than_x.reverse()
        
        if (head != None and head.val < x):
            less_than_x.append(head.val)
            head = head.next

        for num in less_than_x:
            tmp = ListNode(num)
            tmp.next = head
            head = tmp
        
        return head



                
