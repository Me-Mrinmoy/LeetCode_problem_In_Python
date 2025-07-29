class Solution:
    def findDuplicates(self, nums):
        result = []

        for num in nums:
            index = abs(num) - 1  # correct index

            if nums[index] < 0:
                # already visited => duplicate
                result.append(abs(num))
            else:
                # mark as visited
                nums[index] = -nums[index]

        return result
