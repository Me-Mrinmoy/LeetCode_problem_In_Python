class Solution:
    def canJump(self, nums):  # Removed type hinting
        max_reachable = 0
        n = len(nums)

        for i in range(n):
            if i > max_reachable:
                return False  # Cannot reach this index
            max_reachable = max(max_reachable, i + nums[i])
            if max_reachable >= n - 1:
                return True  # Can reach the last index

        return False  # If we exit the loop without reaching the last index

# Example usage:
nums = [2, 3, 1, 1, 4]
solution = Solution()
print(solution.canJump(nums))  # Output: True
