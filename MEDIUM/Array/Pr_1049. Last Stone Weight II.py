class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #Memoization
        def findMaxTarget(start, targetSum, dp):
            if start < 0 or targetSum == 0:
                return 0

            if dp[start][targetSum] != -1:
                return dp[start][targetSum]

            if targetSum >= stones[start]:
                dp[start][targetSum] = max(findMaxTarget(start - 1, targetSum, dp), stones[start] + findMaxTarget(start - 1, targetSum - stones[start], dp))
            else:
                dp[start][targetSum] = findMaxTarget(start - 1, targetSum, dp)
            
            return dp[start][targetSum]

        l = len(stones)
        totalSum = 0
        for s in stones:
            totalSum += s

        target = totalSum // 2
        dp = [[-1] * (target + 1) for _ in range(l+1)]
        maxSum = findMaxTarget(l - 1, target, dp)
        return totalSum - maxSum - maxSum


        #Tabulation
        l = len(stones)
        totalSum = 0
        for s in stones:
            totalSum += s

        target = totalSum // 2
        dp = [[0] * (target + 1) for _ in range(l+1)]

        for i in range(1, l+1):
            for j in range(target + 1):
                if j >= stones[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], stones[i - 1] + dp[i - 1][j - stones[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]

        return totalSum - (2 * dp[l][target])


        #Space optimization - 1
        l = len(stones)
        totalSum = 0
        for s in stones:
            totalSum += s

        target = totalSum // 2
        dp = [0] * (target + 1)

        for i in range(1, l+1):
            curr = [0] * (target + 1)
            for j in range(target + 1):
                if j >= stones[i - 1]:
                    curr[j] = max(dp[j], stones[i - 1] + dp[j - stones[i - 1]])
                else:
                    curr[j] = dp[j]
            dp = curr

        return totalSum - (2 * dp[target])


        #Space optimization - 2
        totalSum = 0
        for s in stones:
            totalSum += s

        target = totalSum // 2
        dp = [0] * (target + 1)

        for s in stones:
            for j in range(target, s - 1, -1):
                dp[j] = max(dp[j], s + dp[j - s])

        return totalSum - (2 * dp[target])
