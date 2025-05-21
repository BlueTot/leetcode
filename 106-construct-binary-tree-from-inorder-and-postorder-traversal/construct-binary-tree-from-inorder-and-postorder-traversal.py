# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indices = {v : k for k, v in enumerate(inorder)}

        def construct(p1, p2, i1, i2):
            print(p1, p2, i1, i2)
            if p2 < p1 or i2 < i1:
                return None
            if p2 == p1 and i1 == i2:
                return TreeNode(postorder[p2])
            node = TreeNode(postorder[p2]) # the root is at the start
            left = indices[postorder[p2]] - i1
            right = i2 - indices[postorder[p2]]
            node.left = construct(p1, p1 + left - 1, i1, i1 + left - 1)
            node.right = construct(p1 + left, p1 + left + right - 1, indices[postorder[p2]] + 1, indices[postorder[p2]] + right)
            return node
        
        return construct(0, len(postorder)-1, 0, len(inorder)-1)