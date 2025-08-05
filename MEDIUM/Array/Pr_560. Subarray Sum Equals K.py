from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        count = defaultdict(int)
        count[0] = 1  # handles exact matches from start
        prefix_sum = 0
        ans = 0

        for num in nums:
            prefix_sum += num
            ans += count[prefix_sum - k]
            count[prefix_sum] += 1

        return ans
