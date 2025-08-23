class Solution:
    def sumSubseqWidths(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        ans = 0
        for i, x in enumerate(nums):
            ans = (ans + (pow2[i] - pow2[n-1-i]) * x) % MOD
        
        return ans
