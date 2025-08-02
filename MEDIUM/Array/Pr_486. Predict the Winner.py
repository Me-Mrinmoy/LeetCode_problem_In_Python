class Solution:
    def predictTheWinner(self, nums):
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == j:
                return nums[i]
            pick_left = nums[i] - dp(i + 1, j)
            pick_right = nums[j] - dp(i, j - 1)
            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]

        return dp(0, len(nums) - 1) >= 0
