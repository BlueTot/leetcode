class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # find insert position using binary search
        def search(intervals, newInterval):
            left = 0
            right = len(intervals)

            while left < right:
                mid = (left + right) // 2
                if intervals[mid][0] >= newInterval[0]:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        # merge last interval in new array with new interval
        def handle(new, interval):
            s1, e1 = new[-1]
            s2, e2 = interval
            if s2 <= e1:
                new[-1] = [s1, max(e1, e2)]
            else:
                new.append([s2, e2])
        
        insertPosition = search(intervals, newInterval)

        if insertPosition == 0:
            # if we insert at the start, set base to be new interval
            new = [newInterval] 
        else:
            # otherwise, put in all intervals before the insert position
            # and handle the new interval
            new = [*intervals[:insertPosition]]
            handle(new, newInterval)

        # handle the remaining intervals after the insert position
        for i in range(insertPosition, len(intervals)):
            handle(new, intervals[i])

        return new