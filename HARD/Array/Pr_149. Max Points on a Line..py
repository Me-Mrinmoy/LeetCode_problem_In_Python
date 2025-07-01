from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
        
        max_points = 1  # Minimum is 1 since we have at least one point

        for i in range(len(points)):
            slopes = defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue  # Skip the same point
                x1, y1 = points[i]
                x2, y2 = points[j]

                # Calculate slope as a reduced fraction (dy/dx)
                dx = x2 - x1
                dy = y2 - y1
                
                # Handle vertical lines separately
                if dx == 0:  # Vertical line
                    slope = ('inf', 0)  # Use 'inf' to denote vertical slope
                elif dy == 0:  # Horizontal line
                    slope = (0, 'inf')  # Use 'inf' to denote horizontal slope
                else:
                    g = self.gcd(dx, dy)  # Get gcd to reduce the slope
                    slope = (dy // g, dx // g)  # Store slope as (dy, dx)

                slopes[slope] += 1
            
            # Find the maximum points on the same line for this point
            current_max = max(slopes.values()) + 1 if slopes else 1  # +1 for the current point
            max_points = max(max_points, current_max)

        return max_points

    # GCD function
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

# Example usage
solution = Solution()
points = [[1, 1], [2, 2], [3, 3]]
result = solution.maxPoints(points)
print(result)  # Output: 3
