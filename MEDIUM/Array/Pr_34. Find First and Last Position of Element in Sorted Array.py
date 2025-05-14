class Solution:
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first_index = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    first_index = mid  # Update first_index
                    right = mid - 1  # Continue searching in the left half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return first_index
        
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last_index = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    last_index = mid  # Update last_index
                    left = mid + 1  # Continue searching in the right half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return last_index

        first = findFirst(nums, target)
        last = findLast(nums, target)
        
        return [first, last]

# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8
solution = Solution()
result = solution.searchRange(nums, target)
print(result)  # Output: [3, 4]
