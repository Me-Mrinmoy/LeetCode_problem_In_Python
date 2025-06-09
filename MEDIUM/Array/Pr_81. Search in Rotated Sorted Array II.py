class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True  # Target found
            
            # Handle the case where duplicates are present
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in the left half
                else:
                    left = mid + 1   # Target is in the right half
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Target is in the right half
                else:
                    right = mid - 1  # Target is in the left half

        return False  # Target not found

# Example usage:
solution = Solution()
nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
print(solution.search(nums, target))  # Output: True
