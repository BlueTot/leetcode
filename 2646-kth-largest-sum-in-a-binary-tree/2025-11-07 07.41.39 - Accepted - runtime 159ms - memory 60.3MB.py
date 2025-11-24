# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        levels = []

        def populate(node, level):
            nonlocal levels

            if node is None:
                return

            if level >= len(levels):
                levels.append(0)
            levels[level] += node.val

            populate(node.left, level + 1)
            populate(node.right, level + 1)
        
        populate(root, 0)

        if len(levels) < k:
            return -1

        levels.sort(reverse=True)
        return levels[k-1]
