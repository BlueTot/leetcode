from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        queue = deque([start])
        visited = set()

        while queue:
            index = queue.popleft()
            if arr[index] == 0:
                return True
            visited.add(index)
            for neighbour in (index + arr[index], index - arr[index]):
                if 0 <= neighbour < len(arr) and neighbour not in visited:
                    queue.append(neighbour)
        
        return False
