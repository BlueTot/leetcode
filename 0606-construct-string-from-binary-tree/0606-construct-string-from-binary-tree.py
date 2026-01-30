# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        elif root.left is None and root.right is None:
            return f"{root.val}"
        elif root.left is not None and root.right is None:
            return f"{root.val}({self.tree2str(root.left)})"
        elif root.left is None and root.right is not None:
            return f"{root.val}()({self.tree2str(root.right)})"
        else:
            return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"