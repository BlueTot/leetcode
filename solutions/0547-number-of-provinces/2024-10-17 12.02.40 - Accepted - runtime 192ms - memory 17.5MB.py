class Solution:

    def traverse(self, node, isConnected, visited):
        if node not in visited:
            visited.add(node)
            for neighbour, val in enumerate(isConnected[node]):
                if node != neighbour and val == 1:
                    self.traverse(neighbour, isConnected, visited)
                
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = set(range(len(isConnected)))
        visited = set()
        provinces = 0
        while cities - visited:
            self.traverse(list(cities - visited)[0], isConnected, visited)
            provinces += 1
        return provinces
