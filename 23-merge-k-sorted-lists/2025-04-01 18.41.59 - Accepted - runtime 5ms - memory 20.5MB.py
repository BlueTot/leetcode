# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappop, heappush
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for ll in lists:
            curr = ll
            while (curr != None):
                heappush(pq, curr.val)
                curr = curr.next
        newlist = ListNode()
        curr = newlist
        if not pq:
            return None
        while pq:
            num = heappop(pq)
            curr.val = num
            if (len(pq) == 0):
                curr.next = None
            else:
                curr.next = ListNode()
            curr = curr.next
        return newlist
        
