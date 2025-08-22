from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        layers = []
        queue = deque([(root, 0)])
        if root == None:
            return []
        while queue:
            node, layer = queue.popleft()
            if len(layers) < layer + 1:
                layers.append([])
            layers[-1].append(node.val)
            if node.left != None:
                queue.append((node.left, layer + 1))
            if node.right != None:
                queue.append((node.right, layer + 1))
        return [layer[::-1] if i % 2 == 1 else layer for i, layer in enumerate(layers)]