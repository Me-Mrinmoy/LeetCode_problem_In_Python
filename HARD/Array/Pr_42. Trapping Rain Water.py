class Solution:
    def trap(self, height):
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        water_trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    water_trapped += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    water_trapped += max_right - height[right]
                right -= 1
        
        return water_trapped

# Example usage:
solution = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
output = solution.trap(height)
print(output)  # Output should be 6
