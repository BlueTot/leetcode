# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        index = 1
        curr = head
        while (curr != None): 
            if index == left:    
                before = prev
                prev = None
                start = curr
                while (index <= right):
                    nextNode = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nextNode
                    index += 1
                start.next = curr
                if before is not None:
                    before.next = prev
                    return head
                else:
                    return prev
            else:
                prev = curr
                curr = curr.next
                index += 1
        return head


            
                