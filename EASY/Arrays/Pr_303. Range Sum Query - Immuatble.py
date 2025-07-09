class NumArray:

    def __init__(self, nums):
        # Create a prefix sum array where prefix[i] is sum of nums[0] to nums[i - 1]
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        # sum from left to right is prefix[right + 1] - prefix[left]
        return self.prefix[right + 1] - self.prefix[left]
