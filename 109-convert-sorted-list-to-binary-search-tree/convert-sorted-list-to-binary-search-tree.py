# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next

        def convert(a, b):
            if b < a:
                return None
            mid = (a + b) // 2
            node = TreeNode(nums[mid])
            node.left = convert(a, mid-1)
            node.right = convert(mid+1, b)
            return node
        
        return convert(0, len(nums)-1)