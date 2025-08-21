from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        graph = {}
        for u, v in redEdges:
            if (u, 0) not in graph:
                graph[(u, 0)] = set()
            graph[(u, 0)].add((v, 1))
        for u, v in blueEdges:
            if (u, 1) not in graph:
                graph[(u, 1)] = set()
            graph[(u, 1)].add((v, 0))
        
        queue = deque([((0, 0), 0), ((0, 1), 0)])
        visited = set()
        shortests = [-1 for _ in range(n)]

        while queue:
            node, dist = queue.popleft()
            if shortests[node[0]] == -1:
                shortests[node[0]] = dist
            if node in visited:
                continue
            visited.add(node)
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    queue.append((neighbour, dist + 1))
        
        return shortests