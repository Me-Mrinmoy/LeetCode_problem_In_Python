from collections import defaultdict

class Solution:
    def minAreaRect(self, points):
        # map x -> set of y's
        x_map = defaultdict(set)
        for x, y in points:
            x_map[x].add(y)

        min_area = float("inf")
        x_coords = list(x_map.keys())

        # check all pairs of x
        for i in range(len(x_coords)):
            for j in range(i + 1, len(x_coords)):
                x1, x2 = x_coords[i], x_coords[j]
                # common y's
                common_y = x_map[x1] & x_map[x2]
                if len(common_y) >= 2:
                    sorted_y = sorted(common_y)
                    for k in range(1, len(sorted_y)):
                        area = abs(x2 - x1) * (sorted_y[k] - sorted_y[k - 1])
                        min_area = min(min_area, area)

        return 0 if min_area == float("inf") else min_area
