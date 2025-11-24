from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        layers = []
        queue = deque([(root, 0)])
        while queue:
            node, layer = queue.popleft()
            if len(layers) < layer + 1:
                layers.append([])
            layers[-1].append(node.val if node != None else None)
            if node != None:
                queue.append((node.left, layer + 1))
                queue.append((node.right, layer + 1))
        return all(layer == layer[::-1] for layer in layers)
