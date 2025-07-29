from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points):
        res = 0

        for i in points:
            dist_count = defaultdict(int)
            for j in points:
                dx = i[0] - j[0]
                dy = i[1] - j[1]
                dist = dx * dx + dy * dy  # squared distance to avoid floating-point
                dist_count[dist] += 1

            for count in dist_count.values():
                if count > 1:
                    res += count * (count - 1)

        return res
