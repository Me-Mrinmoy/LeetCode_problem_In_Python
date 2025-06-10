class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        max_area = 0
        cols = len(matrix[0])
        heights = [0] * cols  # Initialize heights for the histogram
        
        for row in matrix:
            for i in range(cols):
                # Update the heights
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            # Calculate the maximum rectangle area for the current histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)  # Append a zero height to handle remaining bars in the stack
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Get the height of the popped bar
                w = i if not stack else i - stack[-1] - 1  # Calculate the width
                max_area = max(max_area, h * w)  # Update the max area
            stack.append(i)  # Push the current index onto the stack
        
        return max_area

# Example usage
if __name__ == "__main__":
    solution = Solution()
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    output = solution.maximalRectangle(matrix)
    print(output)  # Output: 6
