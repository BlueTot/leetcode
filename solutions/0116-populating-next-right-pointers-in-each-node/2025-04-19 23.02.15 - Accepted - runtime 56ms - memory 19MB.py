"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([(root, 0)])
        prev = (None, -1)
        while queue:
            node, level = queue.popleft()
            if node is None:
                continue
            if node.left is not None:
                queue.append((node.left, level+1))
            if node.right is not None:
                queue.append((node.right, level+1))
            if prev[0] != None:
                if prev[1] == level:
                    prev[0].next = node
                else:
                    prev[0].next = None
            prev = (node, level)
        return root
