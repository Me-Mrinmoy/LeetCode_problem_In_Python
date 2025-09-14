class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x0, y0), (x1, y1), (x2, y2) = points
        return (y2 - y1) * (x0 - x1) != (x2 - x1) * (y0 - y1)
