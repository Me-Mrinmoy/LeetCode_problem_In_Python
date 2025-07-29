from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        total = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = dp[j][diff]
                
                # Add count to total (only sequences with length ≥ 3)
                total += cnt

                # Extend all sequences ending at j with diff, and
                # start a new pair (j, i) for future sequences
                dp[i][diff] += cnt + 1

        return total
