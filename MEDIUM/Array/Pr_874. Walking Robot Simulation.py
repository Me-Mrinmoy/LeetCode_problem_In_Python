class Solution:
    def robotSim(self, commands, obstacles):
        # Directions: N, E, S, W
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        d = 0  # facing north
        x, y = 0, 0
        obstacles_set = {(ox, oy) for ox, oy in obstacles}
        max_dist = 0

        for cmd in commands:
            if cmd == -2:  # turn left
                d = (d + 3) % 4
            elif cmd == -1:  # turn right
                d = (d + 1) % 4
            else:  # move forward
                dx, dy = dirs[d]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacles_set:
                        break  # blocked by obstacle
                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)

        return max_dist
