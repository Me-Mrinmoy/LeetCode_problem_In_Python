class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # Stack to store the indices of the bars
        max_area = 0  # Variable to store the maximum area
        heights.append(0)  # Append a zero height to handle remaining bars in the stack
        
        for i in range(len(heights)):
            # While the current height is less than the height of the bar at the top of the stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Get the height of the popped bar
                # Calculate the width
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)  # Update the max area
            stack.append(i)  # Push the current index onto the stack
        
        return max_area

# Example usage
if __name__ == "__main__":
    solution = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    output = solution.largestRectangleArea(heights)
    print(output)  # Output: 10
