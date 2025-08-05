class Solution:
    def optimalDivision(self, nums):
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return "{}/{}".format(nums[0], nums[1])
        # Wrap everything except the first in parentheses
        middle = "/".join(str(num) for num in nums[1:])
        return "{}/({})".format(nums[0], middle)
