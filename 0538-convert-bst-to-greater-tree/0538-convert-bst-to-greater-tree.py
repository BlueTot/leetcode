# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def in_order(node):
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [node.val]
            return in_order(node.left) + [node.val] + in_order(node.right)
        
        greater = {}
        total = 0
        for num in reversed(in_order(root)):
            greater[num] = num + total
            total += num
        
        def replace(node):
            if node is None:
                return
            node.val = greater[node.val]
            replace(node.left)
            replace(node.right)
        
        replace(root)
        return root

        