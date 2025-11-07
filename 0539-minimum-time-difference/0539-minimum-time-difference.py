class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        times = []
        for string in timePoints:
            times.append(list(map(int, string.split(":"))))
        
        times.sort()

        def difference(time_a: list[int],  time_b: list[int]) -> int:
            if time_a[0] == time_b[0]: # same hour
                return time_b[1] - time_a[1]
            else: # no modulo
                return ((time_b[0] - time_a[0] + 24) % 24) * 60 + time_b[1] - time_a[1]

        best = float("inf")
        for i in range(0, len(times)):
            curr = difference(times[(i-1)%len(times)], times[i])
            if curr >= 0:
                best = min(best, curr)

        return best