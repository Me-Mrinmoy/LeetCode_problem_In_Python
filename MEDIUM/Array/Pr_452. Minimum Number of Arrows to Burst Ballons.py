class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # Sort intervals by their end point
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        arrow_pos = points[0][1]

        for start, end in points[1:]:
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end  # place new arrow

        return arrows
