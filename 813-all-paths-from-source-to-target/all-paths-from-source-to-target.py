class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        paths = []

        def dfs(node, stack):
            stack.append(node)
            if node == n-1:
                paths.append(stack[:])
            for neighbour in graph[node]:
                dfs(neighbour, stack)
            stack.pop()
        
        dfs(0, [])
        return paths