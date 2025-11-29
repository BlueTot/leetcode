from heapq import heappop, heappush

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        # sort by the start time
        intervals.sort()

        # store last job in each group in min heap
        min_heap = []
        d = 0

        for i in range(len(intervals)):
            if min_heap and min_heap[0][0] < intervals[i][0]:
                curr_group = min_heap[0][1]
                heappop(min_heap)
                heappush(min_heap, (intervals[i][1], curr_group))
            else:
                heappush(min_heap, (intervals[i][1], d))
                d += 1
        
        return d
                
            