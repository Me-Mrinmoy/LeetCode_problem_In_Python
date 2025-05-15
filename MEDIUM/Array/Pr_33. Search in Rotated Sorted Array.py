class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if we found the target
            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:  # Target in the sorted part
                    right = mid - 1  # Search in the left half
                else:
                    left = mid + 1  # Search in the right half
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  # Target in the sorted part
                    left = mid + 1  # Search in the right half
                else:
                    right = mid - 1  # Search in the left half
        
        return -1  # Target not found

# Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
solution = Solution()
index = solution.search(nums, target)
print(index)  # Output: 4
