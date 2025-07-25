class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return len(nums)

        up = down = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1

        return max(up, down)
