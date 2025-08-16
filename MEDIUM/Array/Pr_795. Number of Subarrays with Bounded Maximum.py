class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):
        def count(bound):
            ans = 0
            cur = 0
            for x in nums:
                if x <= bound:
                    cur += 1
                else:
                    cur = 0
                ans += cur
            return ans

        return count(right) - count(left - 1)


# Example usage:
solution = Solution()
print(solution.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))  # Output: 3
print(solution.numSubarrayBoundedMax([2, 9, 2, 5, 6], 2, 8))  # Output: 7
