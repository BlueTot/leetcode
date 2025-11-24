# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = {}
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if level not in levels:
                levels[level] = 0
            levels[level] += node.val
            if node.left is not None:
                queue.append((node.left, level+1))
            if node.right is not None:
                queue.append((node.right, level+1))
        maximas = set()
        maximum = max(levels.values())
        for k, v in levels.items():
            if v == maximum:
                maximas.add(k)
        return min(maximas)