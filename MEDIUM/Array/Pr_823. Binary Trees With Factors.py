class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        index = {x: i for i, x in enumerate(arr)}  # map value → index

        for i, x in enumerate(arr):
            dp[x] = 1  # single-node tree
            for j in range(i):  # check factors smaller than x
                a = arr[j]
                if x % a == 0:
                    b = x // a
                    if b in dp:
                        dp[x] += dp[a] * dp[b]
            dp[x] %= MOD

        return sum(dp.values()) % MOD
