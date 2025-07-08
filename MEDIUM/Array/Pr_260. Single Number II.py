class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num

        # Get the rightmost set bit
        diff = xor & -xor

        a = 0
        b = 0
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num

        return [a, b]

# Example usage:
sol = Solution()
print(sol.singleNumber([1, 2, 1, 3, 2, 5]))  # Output: [3, 5] or [5, 3]
