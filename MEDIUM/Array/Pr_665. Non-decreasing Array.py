class Solution:
    def checkPossibility(self, nums):
        changed = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:  # violation
                if changed:
                    return False
                changed = True
                # Decide whether to lower nums[i] or raise nums[i+1]
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]  # lower nums[i]
                else:
                    nums[i + 1] = nums[i]  # raise nums[i+1]
        return True
