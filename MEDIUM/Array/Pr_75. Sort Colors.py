class Solution:
    def sortColors(self, nums):
        low, current, high = 0, 0, len(nums) - 1
        
        while current <= high:
            if nums[current] == 0:
                # Swap nums[current] with nums[low]
                nums[low], nums[current] = nums[current], nums[low]
                low += 1
                current += 1
            elif nums[current] == 2:
                # Swap nums[current] with nums[high]
                nums[high], nums[current] = nums[current], nums[high]
                high -= 1
            else:
                # Move to the next element
                current += 1

# Example usage:
solution = Solution()
nums1 = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums1)
print(nums1)  # Output: [0, 0, 1, 1, 2, 2]

nums2 = [2, 0, 1]
solution.sortColors(nums2)
print(nums2)  # Output: [0, 1, 2]
