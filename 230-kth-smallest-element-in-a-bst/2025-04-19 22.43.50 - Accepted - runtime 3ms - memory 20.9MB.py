# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inOrder(self, curr: Optional[TreeNode]) -> List[int]:
        if curr is None:
            return []
        if curr.left is None and curr.right is None:
            return [curr.val]
        output = []
        if curr.left is not None:
            output = self.inOrder(curr.left)
        output.append(curr.val)
        if curr.right is not None:
            output.extend(self.inOrder(curr.right))
        return output
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inOrder(root)[k-1]