class Solution:
    def canPartitionKSubsets(self, nums, k):
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target = total_sum // k

        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        buckets = [0] * k

        def backtrack(index):
            if index == len(nums):
                return True  # All numbers placed successfully

            for i in range(k):
                if buckets[i] + nums[index] <= target:
                    buckets[i] += nums[index]
                    if backtrack(index + 1):
                        return True
                    buckets[i] -= nums[index]
                if buckets[i] == 0:
                    break  # Optimization: avoid same empty bucket attempts
            return False

        return backtrack(0)
