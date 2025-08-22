class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        orig = [(a,b) for a, b in intervals]
        indices = {interval[0] : i for i, interval in enumerate(intervals)}
        intervals.sort()
        
        def find(start, end):
            if start == end:
                return indices[start]
            left = 0
            right = len(intervals) - 1
            while left <= right:
                mid = (left + right) // 2
                if mid > 0 and intervals[mid][0] >= end and intervals[mid-1][0] < end:
                    return indices[intervals[mid][0]]
                elif intervals[mid][0] < end:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        return [find(start, end) for start, end in orig]