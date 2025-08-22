# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValid(self, root):
        if root.left is None and root.right is None:
            return root.val, root.val, True
        elif root.left is not None and root.right is None:
            minimum, maximum, valid = self.isValid(root.left)
            return minimum, root.val, maximum < root.val and valid
        elif root.left is None and root.right is not None:
            minimum, maximum, valid = self.isValid(root.right)
            return root.val, maximum, root.val < minimum and valid
        else:
            minimum1, maximum1, valid1 = self.isValid(root.left)
            minimum2, maximum2, valid2 = self.isValid(root.right)
            return minimum1, maximum2, maximum1 < root.val < minimum2 and valid1 and valid2

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root)[2]
        