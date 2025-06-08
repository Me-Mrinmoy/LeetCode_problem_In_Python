class Solution:
    def subsets(self, nums):
        result = []
        self.backtrack(nums, 0, [], result)
        return result

    def backtrack(self, nums, start, path, result):
        # Append the current subset (path) to the result
        result.append(path)
        
        # Explore further subsets
        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            self.backtrack(nums, i + 1, path + [nums[i]], result)

# Example usage:
solution = Solution()

# Example 1
nums1 = [1, 2, 3]
output1 = solution.subsets(nums1)
print(output1)  # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# Example 2
nums2 = [0]
output2 = solution.subsets(nums2)
print(output2)  # Output: [[], [0]]
