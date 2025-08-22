class Solution:
    def traverse(self, node, rooms, visited):
        if node not in visited:
            visited.add(node)
            for room in rooms[node]:
                if room not in visited:
                    self.traverse(room, rooms, visited)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.traverse(0, rooms, visited)
        return visited == set(range(len(rooms)))
            