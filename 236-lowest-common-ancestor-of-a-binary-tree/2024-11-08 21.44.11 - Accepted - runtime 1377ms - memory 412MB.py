# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def traverse(self, root, target, path=[]):
        if root is not None:
            if root == target:
                return path + [root]
            if root.left is not None:
                if (output := self.traverse(root.left, target, path+[root])):
                    return output
            if root.right is not None:
                if (output := self.traverse(root.right, target, path+[root])):
                    return output
        return []

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        prev = None
        for n, m in zip(self.traverse(root, p), self.traverse(root, q)):
            if n.val != m.val:
                return prev
            prev = n
        return prev