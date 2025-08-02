import random
import bisect

class Solution:
    def __init__(self, rects):
        self.rects = rects
        self.prefix_sums = []
        total_points = 0

        for a, b, x, y in rects:
            points = (x - a + 1) * (y - b + 1)
            total_points += points
            self.prefix_sums.append(total_points)

    def pick(self):
        rand_point = random.randint(1, self.prefix_sums[-1])
        rect_index = bisect.bisect_left(self.prefix_sums, rand_point)
        a, b, x, y = self.rects[rect_index]
        width = x - a + 1

        base = self.prefix_sums[rect_index - 1] if rect_index > 0 else 0
        offset = rand_point - base - 1
        dx = offset % width
        dy = offset // width

        return [a + dx, b + dy]
