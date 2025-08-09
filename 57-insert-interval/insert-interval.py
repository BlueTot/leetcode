class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def search(intervals, newInterval):
            left = 0
            right = len(intervals)

            # if newInterval[0] < intervals[0][0]:
            #     return 0
            # elif newInterval[0] > intervals[-1][0]:
            #     return len(intervals)

            while left < right:
                mid = (left + right) // 2
                if intervals[mid][0] >= newInterval[0]:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        def handle(new, interval):
            s1, e1 = new[-1]
            s2, e2 = interval
            if s2 <= e1:
                new[-1] = [s1, max(e1, e2)]
            else:
                new.append([s2, e2])
        
        insertPosition = search(intervals, newInterval)
        print(insertPosition)
        if insertPosition == 0:
            new = [newInterval] 
        else:
            new = [*intervals[:insertPosition]]
            handle(new, newInterval)

        print(new)
        print(intervals)
        for i in range(insertPosition, len(intervals)):
            handle(new, intervals[i])

        return new