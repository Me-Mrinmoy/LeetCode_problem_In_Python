class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:  # Minimum must be in the right part
                left = mid + 1
            elif nums[mid] < nums[right]:  # Minimum is in the left part
                right = mid
            else:  # nums[mid] == nums[right], we cannot determine the sorted side
                right -= 1  # Decrease right pointer
            
        return nums[left]

# Example usage
solution = Solution()
nums = [1, 3, 5]
result = solution.findMin(nums)
print(result)  # Output: 1
