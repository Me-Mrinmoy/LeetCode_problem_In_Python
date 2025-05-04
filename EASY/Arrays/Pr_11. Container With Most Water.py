class Solution:
    def maxArea(self, height):
        # Initialize two pointers
        left = 0
        right = len(height) - 1
        max_area = 0
        
        # Loop until the two pointers meet
        while left < right:
            # Calculate the area between the lines at left and right
            width = right - left
            current_area = min(height[left], height[right]) * width
            
            # Update the maximum area if the current one is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer of the smaller height inwards
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Example usage:
height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))  # Output: 49
