# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        x, y = l1, l2
        while x is not None and y is not None:
            x, y = x.next, y.next
        if x is None and y is not None:
            curr, adj = l2, l1
            base = l2
        elif x is not None and y is None:
            curr, adj = l1, l2
            base = l1
        else:
            curr, adj = l1, l2
            base = l1

        carry = 0
        while curr is not None:
            if adj is None:
                digit, carry = (v := curr.val + carry) % 10, v // 10
                curr.val = digit
                if curr.next is None and carry != 0:
                    curr.next = ListNode(carry)
                    return base
                curr = curr.next
            else:
                digit, carry = (v := curr.val + adj.val + carry) % 10, v // 10
                curr.val = digit
                if curr.next is None and carry != 0:
                    curr.next = ListNode(carry)
                    return base
                curr = curr.next
                adj = adj.next
    
        return base

        