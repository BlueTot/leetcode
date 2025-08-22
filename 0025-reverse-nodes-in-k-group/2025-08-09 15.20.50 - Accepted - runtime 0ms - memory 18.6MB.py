# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # function to get length of linked list
        def length(head):
            curr = head
            length = 0
            while curr != None:
                curr = curr.next
                length += 1
            return length
        
        new_head = head
        prev_segment = None
        curr = head

        # repeat this length // k times so we don't overflow
        for i in range(length(head) // k):

            # record the start of the segment
            start = curr
            prev = curr
            curr = curr.next # advance to next node so we can reverse

            # for remaining k-1 nodes, we reverse the link and move to next node.
            for j in range(k-1):
                next_node = curr.next
                curr.next = prev
                prev = curr
                if j == k-2: # if at the end
                    if i == 0: # if we are on first segment, save the head
                        new_head = curr
                    else: # otherwise, connect the segments
                        prev_segment.next = curr
                curr = next_node
            
            # update the segment pointers
            start.next = curr
            prev_segment = start

        return new_head