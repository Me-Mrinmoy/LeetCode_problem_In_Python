class Solution:
    def totalHammingDistance(self, nums):
        total = 0
        n = len(nums)
        
        for i in range(32):  # for 32-bit integers
            count_ones = sum((num >> i) & 1 for num in nums)
            count_zeros = n - count_ones
            total += count_ones * count_zeros
        
        return total
