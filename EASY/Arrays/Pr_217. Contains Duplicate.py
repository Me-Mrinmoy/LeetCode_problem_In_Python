class Solution:
    def containsDuplicate(self, nums):
        seen = set()  # Set to store unique elements
        for num in nums:
            if num in seen:  # If the number is already in the set, return True
                return True
            seen.add(num)  # Add the number to the set if not already present
        return False  # If no duplicates are found, return False

# Example usage
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 1]
print(solution.containsDuplicate(nums1))  # Output: True

# Example 2
nums2 = [1, 2, 3, 4]
print(solution.containsDuplicate(nums2))  # Output: False

# Example 3
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(solution.containsDuplicate(nums3))  # Output: True
