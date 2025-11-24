# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def binSearch(self, curr, p):
        while (curr.val != p.val):
            if p.val < curr.val:
                return [curr] + self.binSearch(curr.left, p)
            elif p.val > curr.val:
                return [curr] + self.binSearch(curr.right, p)
        return [p]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        path1, path2 = self.binSearch(root, p), self.binSearch(root, q)
        prev = None
        for n1, n2 in zip(path1, path2):
            if n1.val != n2.val:
                return prev
            prev = n1
        return prev