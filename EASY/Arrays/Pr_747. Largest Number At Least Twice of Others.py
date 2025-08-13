class Solution:
    def dominantIndex(self, nums):
        # Find the maximum value and its index
        max_val = max(nums)
        max_index = nums.index(max_val)
        
        # Check if max_val is at least twice every other number
        for i, num in enumerate(nums):
            if i != max_index and max_val < 2 * num:
                return -1
        
        return max_index


# Example usage:
print(Solution().dominantIndex([3, 6, 1, 0]))  # Output: 1
print(Solution().dominantIndex([1, 2, 3, 4]))  # Output: -1
