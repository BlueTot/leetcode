"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def clone(node, visited):
            if node == None:
                return None
            if node.val in visited:
                return
            visited[node.val] = Node(val=node.val)
            for neighbour in node.neighbors:
                if neighbour.val not in visited:
                    visited[node.val].neighbors.append(clone(neighbour, visited))
                else:
                    visited[node.val].neighbors.append(visited[neighbour.val])
            return visited[node.val]
        
        return clone(node, {})
