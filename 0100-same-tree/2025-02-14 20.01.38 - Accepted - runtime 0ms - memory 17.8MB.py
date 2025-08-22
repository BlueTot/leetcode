# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None) != (q is None):
            return False
        if p is not None:
            if p.val != q.val:
                return False
            if ((p.left is None) != (q.left is None)) or ((p.right is None) != (q.right is None)):
                return False
            output = True
            if p.left is not None:
                output = output and self.isSameTree(p.left, q.left)
            if p.right is not None:
                output = output and self.isSameTree(p.right, q.right)
            return output
        else:
            return True
        