class Solution:
    def splitArray(self, nums, k):
        def can_split(max_sum):
            count = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > max_sum:
                    count += 1
                    current_sum = num
                else:
                    current_sum += num
            return count <= k

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left
