from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def weight(x, y):
            return -(x*x + y*y)
        
        min_heap = []
        for x, y in points:
            heappush(min_heap, (weight(x,y), (x, y)))
            if len(min_heap) > k:
                heappop(min_heap)
        
        res = []
        while min_heap:
            res.append(heappop(min_heap)[1])
        
        return res