class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left  # This will be the insertion point if target is not found

# Example usage:
nums = [1, 3, 5, 6]
target = 5
solution = Solution()
result = solution.searchInsert(nums, target)
print(result)  # Output: 2
