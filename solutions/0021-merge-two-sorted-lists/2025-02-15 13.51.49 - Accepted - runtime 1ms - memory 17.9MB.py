# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        prev = ListNode()
        prev.next = ListNode()
        head = prev.next
        orig = prev
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                head.val = list1.val
                list1 = list1.next
            else:
                head.val = list2.val
                list2 = list2.next
            head.next = ListNode()
            prev = prev.next
            head = head.next

        if list1 is not None:
            prev.next = list1
        elif list2 is not None:
            prev.next = list2
        else:
            prev.next = None
        return orig.next
            
        