# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # we build a list of nodes
        nodes = []
        curr = head
        while (curr != None):
            nodes.append(curr)
            curr = curr.next

        # two pointers
        i, j = 0, len(nodes) - 1
        start, end = nodes[i], nodes[j]

        while (i < j):

            start.next = end

            if (j != i + 1):
                end.next = nodes[i+1]
            else:
                # terminate if even length
                end.next = None

            i += 1
            j -= 1
            start = nodes[i]
            end = nodes[j]

            # terminate if odd length
            if (i == j):
                end.next = None

        return None