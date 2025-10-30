class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        children = {}
        for i, parent in enumerate(manager):
            if parent not in children:
                children[parent] = []
            children[parent].append(i)
        
        def time(node):
            largest = 0
            for child in children.get(node, []):
                largest = max(largest, time(child))
            return informTime[node] + largest
        
        return time(headID)
