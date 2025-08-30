class Solution:
    def repeatedNTimes(self, nums):
        for k in range(1, 4):
            for i in range(len(nums) - k):
                if nums[i] == nums[i+k]:
                    return nums[i]
