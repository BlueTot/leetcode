class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        for start, end in connections:
            if start not in graph: graph[start] = {}
            graph[start][end] = 1 # forward edge
            if end not in graph: graph[end] = {}
            graph[end][start] = 0 # backward edge
        
        def dfs(node, visited):
            visited.add(node)
            steps = 0
            for neighbour, isForward in graph[node].items():
                if neighbour not in visited:
                    steps += dfs(neighbour, visited) + isForward
            return steps
        
        return dfs(0, set())