class Solution:
    def escapeGhosts(self, ghosts, target):
        # My Manhattan distance from (0,0) to target
        my_dist = abs(target[0]) + abs(target[1])

        # If any ghost can reach the target in <= my_dist, I cannot escape
        for gx, gy in ghosts:
            if abs(gx - target[0]) + abs(gy - target[1]) <= my_dist:
                return False
        return True
