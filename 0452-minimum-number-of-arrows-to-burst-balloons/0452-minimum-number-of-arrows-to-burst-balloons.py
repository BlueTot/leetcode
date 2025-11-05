class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda t : t[0])
        intersect = points[0]
        count = 1

        for i in range(1, len(points)):

            if points[i][0] > intersect[1]: # no overlap
                intersect = points[i]
                count += 1
            elif points[i][1] < intersect[1]: # full overlap
                intersect = points[i]
            else:
                intersect = [points[i][0], intersect[1]]
            
        return count
