class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        safe = [True for _ in range(len(graph))]
        visited = set()

        def dfs(node, stack):
            # print(node, stack)
            if node in stack:
                safe[node] = False
                return
            if node in visited:
                return
            visited.add(node)
            stack.add(node)
            for neighbour in graph[node]:
                dfs(neighbour, stack)
                if not safe[neighbour]:
                    safe[node] = False
            stack.remove(node)

        for i in range(len(graph)):
            if i not in visited:
                # print(i)
                dfs(i, set()) 
        
        return [i for i in range(len(graph)) if safe[i]]