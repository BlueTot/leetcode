from functools import cache

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def max_money(root, taken):
            if root is None:
                return 0
            if taken:
                res = max_money(root.left, False) + max_money(root.right, False)
            else:
                res = max(
                    root.val + max_money(root.left, True) + max_money(root.right, True),
                    max_money(root.left, False) + max_money(root.right, False)
                )
            return res
        
        return max_money(root, False)