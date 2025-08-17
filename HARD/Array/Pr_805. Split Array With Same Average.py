class Solution(object):
    def splitArraySameAverage(self, nums):
        n = len(nums)
        S = sum(nums)

        # Early pruning
        possible = False
        for k in range(1, n):
            if S * k % n == 0:
                possible = True
                break
        if not possible:
            return False

        # DP: dp[k] = set of achievable sums with k elements
        dp = [set() for _ in range(n+1)]
        dp[0].add(0)

        for num in nums:
            # update in reverse order to avoid reuse
            for k in range(n-1, 0, -1):
                for prev in dp[k-1]:
                    dp[k].add(prev + num)

        for k in range(1, n):
            if S * k % n == 0:
                target = S * k // n
                if target in dp[k]:
                    return True

        return False
