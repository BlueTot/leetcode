class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda t : t[0])
        # print(points)
        new = [points[0]]

        for i in range(1, len(points)):

            if points[i][0] > new[-1][1]: # no overlap
                new.append(points[i])
            elif points[i][1] < new[-1][1]: # full overlap
                new[-1] = points[i]
            else:
                new[-1] = [points[i][0], new[-1][1]]
            
            # print(new)
        
        # print(new)
        
        return len(new)


