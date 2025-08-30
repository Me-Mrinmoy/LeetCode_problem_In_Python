class Solution:
    def minAreaFreeRect(self, points):
        point_set = set(map(tuple, points))
        n = len(points)
        min_area = float("inf")

        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if j == i: continue
                x2, y2 = points[j]
                for k in range(n):
                    if k == i or k == j: continue
                    x3, y3 = points[k]

                    # Check if angle at (x2, y2) is 90 degrees
                    v1x, v1y = x1 - x2, y1 - y2
                    v2x, v2y = x3 - x2, y3 - y2
                    if v1x * v2x + v1y * v2y != 0:
                        continue  # not perpendicular

                    # 4th point D
                    dx, dy = x1 + x3 - x2, y1 + y3 - y2
                    if (dx, dy) not in point_set:
                        continue

                    # area = |AB| * |BC|
                    ab2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
                    bc2 = (x3 - x2) ** 2 + (y3 - y2) ** 2
                    area = (ab2 ** 0.5) * (bc2 ** 0.5)
                    if area > 0:
                        min_area = min(min_area, area)

        return 0 if min_area == float("inf") else min_area
