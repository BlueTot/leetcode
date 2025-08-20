class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda i: i[1])
        new_intervals = [intervals[0]]
        count = 0

        print(intervals)

        for i in range(1, len(intervals)):
            if intervals[i][0] < new_intervals[-1][1]: # overlapping
                if intervals[i][1] < new_intervals[-1][1]:
                    new_intervals[-1] = intervals[i]
                count += 1
            else:
                new_intervals.append(intervals[i])
        
        print(new_intervals)
        return count