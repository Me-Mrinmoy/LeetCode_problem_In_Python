class Solution:
    def maxAbsValExpr(self, xs, ys):
        return max(
            abs(x1 - x2) + abs(y1 - y2) + abs(i - j)
            for i, (x1, y1) in enumerate(zip(xs, ys))
            for j, (x2, y2) in enumerate(zip(xs, ys))
        )
