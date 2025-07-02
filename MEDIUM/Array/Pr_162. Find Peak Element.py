class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Compare mid with its right neighbor
            if nums[mid] < nums[mid + 1]:
                left = mid + 1  # Move to the right half
            else:
                right = mid  # Move to the left half including mid

        return left  # left will be the peak index

# Example usage:
solution = Solution()
nums = [1, 2, 3, 1]
print(solution.findPeakElement(nums))  # Output: 2
