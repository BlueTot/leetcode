# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [node.val]
        return self.traverse(node.left) + self.traverse(node.right)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.traverse(root1) == self.traverse(root2)
        