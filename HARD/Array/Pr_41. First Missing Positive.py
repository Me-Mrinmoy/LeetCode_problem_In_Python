class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Step 1: Place each number in its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                target_index = nums[i] - 1
                nums[i], nums[target_index] = nums[target_index], nums[i]

        # Step 2: Find the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all numbers from 1 to n are present
        return n + 1

# Example usage:
solution = Solution()
nums = [1, 2, 0]
output = solution.firstMissingPositive(nums)
print(output)  # Output: 3
