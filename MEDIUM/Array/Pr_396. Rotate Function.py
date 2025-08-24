class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)

        # Compute F(0)
        f = sum(i * num for i, num in enumerate(nums))
        result = f

        # Compute F(k) using recurrence
        for k in range(1, n):
            f = f + total - n * nums[-k]
            result = max(result, f)

        return result


# Example usage:
solution = Solution()
print(solution.maxRotateFunction([4,3,2,6]))  # Output: 26
print(solution.maxRotateFunction([100]))      # Output: 0
