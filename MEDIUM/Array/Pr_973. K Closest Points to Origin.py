class Solution:
    def kClosest(self, points, k):
        # Sort points by squared distance from origin
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]


# Example usage
sol = Solution()
print(sol.kClosest([[1,3],[-2,2]], 1))   # [[-2,2]]
print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))  # [[3,3],[-2,4]]
