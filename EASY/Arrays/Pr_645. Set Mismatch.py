class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        set_nums = set(nums)
        
        sum_actual = sum(nums)
        sum_unique = sum(set_nums)
        expected_sum = n * (n + 1) // 2

        duplicate = sum_actual - sum_unique
        missing = expected_sum - sum_unique

        return [duplicate, missing]
