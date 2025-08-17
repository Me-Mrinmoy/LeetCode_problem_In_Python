class Solution(object):
    def xorGame(self, nums):
        x = 0
        for v in nums:
            x ^= v
        # Alice wins if initial XOR is 0, or if array length is even
        return x == 0 or (len(nums) % 2 == 0)
