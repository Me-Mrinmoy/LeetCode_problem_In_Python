class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Check which side is sorted
            if nums[mid] > nums[right]:  # Mid is in the left sorted part
                left = mid + 1  # Minimum must be in the right part
            else:  # Mid is in the right sorted part
                right = mid  # Minimum is in the left part including mid
            
        # At the end of the loop, left == right, pointing to the minimum element
        return nums[left]

# Example usage
solution = Solution()
nums = [3, 4, 5, 1, 2]
result = solution.findMin(nums)
print(result)  # Output: 1
