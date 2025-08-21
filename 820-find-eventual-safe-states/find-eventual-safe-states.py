class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        safe = [True for _ in range(len(graph))]
        visited = set()

        def dfs(node, stack):

            # if back edge (in stack), it is not safe.
            if node in stack:
                safe[node] = False
                return

            # if we've seen it before, skip it
            if node in visited:
                return

            visited.add(node)
            stack.add(node)

            for neighbour in graph[node]:

                # traverse to neighbour
                dfs(neighbour, stack)

                # if neighbour isn't safe, current isn't safe
                if not safe[neighbour]:
                    safe[node] = False

            stack.remove(node)

        for i in range(len(graph)):
            # if we haven't visited it, traverse to it
            if i not in visited:
                dfs(i, set()) 
        
        return [i for i in range(len(graph)) if safe[i]]