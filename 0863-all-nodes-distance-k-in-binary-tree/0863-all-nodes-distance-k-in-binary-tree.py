# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        # build graph from tree
        graph = {}

        def dfs(node):

            if node.val not in graph:
                graph[node.val] = []

            if node.left is not None:
                graph[node.val].append(node.left.val)
                if node.left.val not in graph:
                    graph[node.left.val] = []
                graph[node.left.val].append(node.val)
                dfs(node.left)

            if node.right is not None:
                graph[node.val].append(node.right.val)
                if node.right.val not in graph:
                    graph[node.right.val] = []
                graph[node.right.val].append(node.val)
                dfs(node.right)
        
        dfs(root)
        
        # bfs
        queue = deque([(target.val, 0)])
        res = []
        visited = set()

        while queue:
            node, dist = queue.popleft()
            if dist == k:
                res.append(node)
            visited.add(node)
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    queue.append((neighbour, dist + 1))
        
        return res

            
            