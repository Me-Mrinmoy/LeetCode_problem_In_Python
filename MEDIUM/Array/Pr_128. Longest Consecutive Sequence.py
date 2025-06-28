class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Check if it's the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the longest streak
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak

# Example usage:
solution = Solution()

# Example 1
nums1 = [100, 4, 200, 1, 3, 2]
output1 = solution.longestConsecutive(nums1)
print(output1)  # Output: 4

# Example 2
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
output2 = solution.longestConsecutive(nums2)
print(output2)  # Output: 9
