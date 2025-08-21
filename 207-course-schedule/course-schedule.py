class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        for u, v in prerequisites:
            if u not in graph: graph[u] = set()
            graph[u].add(v)
        
        visited = set()
        def dfs(node, stack):
            if node in stack:
                return True
            if node in visited:
                return False
            stack.add(node)
            visited.add(node)
            for neighbour in graph.get(node, []):
                if dfs(neighbour, stack):
                    return True
            stack.remove(node)
            return False
        
        for i in range(numCourses):
            if i not in visited:
                if dfs(i, set()):
                    return False
        return True