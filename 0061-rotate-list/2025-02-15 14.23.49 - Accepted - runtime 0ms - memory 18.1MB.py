# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        vals = []
        # find the length
        length = 0
        curr = head
        while (curr != None):
            vals.append(curr.val)
            curr = curr.next
            length += 1
        
        curr = head
        steps = 0
        while (curr != None):
            curr.val = vals[(steps - k % length) % length]
            curr = curr.next
            steps += 1
        return head
        