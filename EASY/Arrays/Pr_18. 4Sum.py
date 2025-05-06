class Solution:
    def fourSum(self, nums, target):
        # Sort the array to make it easier to avoid duplicates
        nums.sort()
        n = len(nums)
        quadruplets = []
        
        # Iterate through the array for the first two numbers
        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Two pointers for the remaining two numbers
                left = j + 1
                right = n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third number (left pointer)
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        
                        # Skip duplicates for the fourth number (right pointer)
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move both pointers inward
                        left += 1
                        right -= 1
                    
                    elif current_sum < target:
                        left += 1  # We need a larger sum, move the left pointer
                    else:
                        right -= 1  # We need a smaller sum, move the right pointer
        
        return quadruplets

# Example usage:
nums = [1, 0, -1, 0, -2, 2]
target = 0
solution = Solution()
print(solution.fourSum(nums, target))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
