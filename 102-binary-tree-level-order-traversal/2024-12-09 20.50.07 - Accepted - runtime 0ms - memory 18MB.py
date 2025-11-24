# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 1)])
        output = []
        while queue:
            node, level = queue.popleft()
            if node is not None:
                if level > len(output):
                    output.append([])
                output[-1].append(node.val)
                if node.left is not None:
                    queue.append((node.left, level+1))
                if node.right is not None:
                    queue.append((node.right, level+1))
        return output

