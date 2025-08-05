from collections import defaultdict

class Solution:
    def leastBricks(self, wall):
        edge_count = defaultdict(int)

        for row in wall:
            position = 0
            # Skip last brick to avoid the wall edge
            for brick in row[:-1]:
                position += brick
                edge_count[position] += 1

        if edge_count:
            max_edges = max(edge_count.values())
        else:
            max_edges = 0

        return len(wall) - max_edges
