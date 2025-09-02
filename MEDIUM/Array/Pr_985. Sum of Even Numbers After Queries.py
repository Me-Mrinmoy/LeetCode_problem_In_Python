from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Initialize hashmap with indices of even numbers
        hashMap = {}
        for ind, val in enumerate(nums):
            if val % 2 == 0:
                hashMap[ind] = val  

        res = []

        for val, ind in queries:
            old_val = nums[ind]

            # If old value was even, remove it from hashmap
            if old_val % 2 == 0 and ind in hashMap:
                del hashMap[ind]

            # Update the value in nums
            nums[ind] = old_val + val

            # If new value is even, add it to hashmap
            if nums[ind] % 2 == 0:
                hashMap[ind] = nums[ind]

            # Append the current sum of evens
            res.append(sum(hashMap.values()))

        return res
