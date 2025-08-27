from collections import defaultdict

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        count = defaultdict(int)
        count[0] = 1   # empty prefix
        prefix_sum = 0
        ans = 0

        for x in nums:
            prefix_sum += x
            # check if there's a prefix that makes sum = goal
            ans += count[prefix_sum - goal]
            # record current prefix sum
            count[prefix_sum] += 1

        return ans
