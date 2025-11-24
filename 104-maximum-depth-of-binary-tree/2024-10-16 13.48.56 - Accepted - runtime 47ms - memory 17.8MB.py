# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.traverse(root)
    def traverse(self, node, depth=1):
        if node.left is None and node.right is None:
            return depth
        if node.left is None:
            return self.traverse(node.right, depth+1)
        if node.right is None:
            return self.traverse(node.left, depth+1)
        return max(self.traverse(node.left, depth+1), self.traverse(node.right, depth+1))