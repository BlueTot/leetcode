class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {}
        incoming = [0] * numCourses
        for v, u in prerequisites:
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
            incoming[v] += 1
        
        numbering = [-1] * numCourses
        c = numCourses - 1  
        
        def dfs(node, visited, path):
            nonlocal c
            
            if node in path:
                return True

            visited.add(node)
            path.add(node)

            for neighbour in graph.get(node, []):
                if neighbour in path:
                    return True
                if neighbour not in visited and dfs(neighbour, visited, path):
                    return True
            
            path.remove(node)
            numbering[node] = c
            c -= 1

            return False


        visited = set()

        for node in range(numCourses):
            if node not in visited and incoming[node] == 0:
                has_cycle = dfs(node, visited, set())
                if has_cycle:
                    return []
        
        if len(visited) < numCourses:
            return []

        res = [0] * numCourses
        for node in range(numCourses):
            res[numbering[node]] = node
        
        return res
