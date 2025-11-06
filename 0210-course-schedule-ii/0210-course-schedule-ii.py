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
    
        # def has_cycle(node, path):
        #     if node in path:
        #         return True
        #     path.add(node)
        #     for neighbour in graph.get(node, []):
            
        
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

            print(node, c)
            numbering[node] = c
            c -= 1

            return False


        visited = set()
        print(graph)

        for node in range(numCourses):
            if node not in visited and incoming[node] == 0:
                has_cycle = dfs(node, visited, set())
                print(has_cycle)
                if has_cycle:
                    return []
        
        print(visited)
        
        if len(visited) < numCourses:
            return []
        
        print(numbering)

        res = [0] * numCourses
        for node in range(numCourses):
            res[numbering[node]] = node
        
        return res

        
        # print(incoming, graph)
        # has_incoming = False
        # visited = set()
        # for node in range(numCourses):
        #     if node not in visited and incoming[node] == 0: # we can start here
        #         has_incoming = True
        #         has_cycle = dfs(node, visited, set())
        #         print(has_cycle)
        #         if has_cycle:
        #             return []
        
        # print(visited)
        # # no entry point
        # if not has_incoming or len(visited) < numCourses:
        #     return []
        
        # print(numbering)
        # res = [0] * numCourses
        # for node in range(numCourses):
        #     res[numbering[node]] = node

        # return res


