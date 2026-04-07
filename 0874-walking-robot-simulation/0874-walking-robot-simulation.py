class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        forbidden_y = {}
        forbidden_x = {}

        for x, y in obstacles:
            if y not in forbidden_y: forbidden_y[y] = []
            forbidden_y[y].append(x)

            if x not in forbidden_x: forbidden_x[x] = []
            forbidden_x[x].append(y)
        
        for k in forbidden_y:
            forbidden_y[k].sort()
        for k in forbidden_x:
            forbidden_x[k].sort()
        
        max_dist = 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        x, y = 0, 0

        for command in commands:

            if command == -1:
                curr_dir = (curr_dir + 1) % 4
            
            elif command == -2:
                curr_dir = (curr_dir - 1) % 4
            
            else:
                dx, dy = direction[curr_dir]
                nx = x + dx * command
                ny = y + dy * command
                skip = False

                # obstacle detection
                if curr_dir == 0: # north, x does not change, y increasing
                    # print(0, command, y, ny, forbidden_x.get(x, []))
                    for fy in forbidden_x.get(x, []):
                        if y < fy <= ny:
                            y = fy - 1
                            skip = True
                            break
                
                elif curr_dir == 2: # south, x does not change, y decreasing
                    # print(2, command, y, ny, forbidden_x.get(x, []))
                    for fy in reversed(forbidden_x.get(x, [])):
                        if y > fy >= ny:
                            y = fy + 1
                            skip = True
                            break

                elif curr_dir == 1: # east, y does not change, x increasing
                    # print(1, command, x, nx, forbidden_y.get(y, []))
                    for fx in forbidden_y.get(y, []):
                        if x < fx <= nx:
                            x = fx - 1
                            skip = True
                            break
                
                else: # west, y does not change, x decreasing
                    # print(3, command, x, nx, forbidden_y.get(y, []))
                    for fx in reversed(forbidden_y.get(y, [])):
                        if x > fx >= nx:
                            x = fx + 1
                            skip = True
                            break
                
                if not skip:
                    x = nx
                    y = ny

                max_dist = max(max_dist, x*x+y*y)
                # print(skip, max_dist)
        
        return max_dist   
