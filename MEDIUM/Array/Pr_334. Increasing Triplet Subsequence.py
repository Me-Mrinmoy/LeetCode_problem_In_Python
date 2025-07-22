class Solution:
    def increasingTriplet(self, nums):
        first = float('inf')  # Smallest element
        second = float('inf')  # Second smallest element
        
        for num in nums:
            if num <= first:
                # Update the smallest element
                first = num
            elif num <= second:
                # Update the second smallest element
                second = num
            else:
                # Found a number greater than first and second
                return True
        
        return False

# Example usage
solution = Solution()

# Test cases
nums1 = [1, 2, 3, 4, 5]
nums2 = [5, 4, 3, 2, 1]
nums3 = [2, 1, 5, 0, 4, 6]

print(solution.increasingTriplet(nums1))  # Output: True
print(solution.increasingTriplet(nums2))  # Output: False
print(solution.increasingTriplet(nums3))  # Output: True
