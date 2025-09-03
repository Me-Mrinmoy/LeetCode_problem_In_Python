from typing import List

class Solution:
    def atLeastK(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        count = {}
        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1
            while len(count) >= k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1

            res += left

        return res

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        a = self.atLeastK(nums, k)
        b = self.atLeastK(nums, k + 1)
        return a - b
