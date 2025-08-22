# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, maximum=-1000000):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1 if node.val >= maximum else 0
        return (1 if node.val >= maximum else 0) + self.traverse(node.left, maximum=max(maximum, node.val)) + self.traverse(node.right, maximum=max(maximum, node.val))

    def goodNodes(self, root: TreeNode) -> int:
        return self.traverse(root)