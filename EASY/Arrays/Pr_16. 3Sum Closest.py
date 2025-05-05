class Solution:
    def threeSumClosest(self, nums, target):
        # Sort the array
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')  # Initialize with a large value
        
        # Iterate through the array
        for i in range(n):
            left = i + 1
            right = n - 1
            
            # Use two pointers to find the closest sum
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If the current sum is closer to the target, update closest_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Adjust pointers
                if current_sum < target:
                    left += 1  # Move left pointer to increase the sum
                elif current_sum > target:
                    right -= 1  # Move right pointer to decrease the sum
                else:
                    # If the current_sum is exactly equal to the target, return it immediately
                    return current_sum
        
        return closest_sum

# Example usage:
nums = [-1, 2, 1, -4]
target = 1
solution = Solution()
print(solution.threeSumClosest(nums, target))  # Output: 2
