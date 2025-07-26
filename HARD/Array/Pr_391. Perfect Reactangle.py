class Solution:
    def isRectangleCover(self, rectangles):
        corners = set()
        area = 0
        min_x = min_y = float('inf')
        max_x = max_y = float('-inf')

        for x1, y1, x2, y2 in rectangles:
            # Update bounding box
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            # Add area
            area += (x2 - x1) * (y2 - y1)

            # Track corners
            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if point in corners:
                    corners.remove(point)
                else:
                    corners.add(point)

        # Final area check
        expected_area = (max_x - min_x) * (max_y - min_y)
        if area != expected_area:
            return False

        # Final corner check
        expected_corners = {
            (min_x, min_y), 
            (min_x, max_y), 
            (max_x, min_y), 
            (max_x, max_y)
        }
        return corners == expected_corners
