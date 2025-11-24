# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        layers = []
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if node is None:
                continue
            if depth == len(layers):
                layers.append([])
            layers[-1].append(node.val)
            if node.left is not None:
                queue.append((node.left, depth+1))
            if node.right is not None:
                queue.append((node.right, depth+1))
        return layers[::-1]
            