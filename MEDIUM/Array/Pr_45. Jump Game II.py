class Solution:
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0  # No jumps needed if there's one or no elements
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):  # We don't need to jump from the last index
            # Update the farthest index we can reach
            farthest = max(farthest, i + nums[i])
            
            # If we reach the end of the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If we can reach the last index, break
                if current_end >= n - 1:
                    break
        
        return jumps

# Example usage:
solution = Solution()
nums = [2, 3, 1, 1, 4]
output = solution.jump(nums)
print(output)  # Output should be 2
