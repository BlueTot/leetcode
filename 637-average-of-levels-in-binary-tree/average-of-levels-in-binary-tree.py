from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        layer = []
        output = []
        curr_layer = 0
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if node == None:
                continue
            if depth > curr_layer:
                output.append(sum(layer)/len(layer))
                layer = []
                curr_layer = depth
            layer.append(node.val)
            if node.left != None:
                queue.append((node.left, depth + 1))
            if node.right != None:
                queue.append((node.right, depth + 1))
        output.append(sum(layer)/len(layer))
        return output
