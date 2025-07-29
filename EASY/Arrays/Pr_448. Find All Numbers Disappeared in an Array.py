class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])  # mark as visited

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)  # i+1 is missing

        return result
