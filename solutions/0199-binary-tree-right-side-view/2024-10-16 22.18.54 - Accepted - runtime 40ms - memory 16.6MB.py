from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([(root, 0)])
        layers = {}
        while queue:
            node, layer = queue.popleft()
            if node is not None:
                if node.left is not None:
                    queue.append((node.left, layer+1))
                if node.right is not None:
                    queue.append((node.right, layer+1))
                layers[layer] = node.val
        if not layers:
            return []
        return list(layers.values())          
        