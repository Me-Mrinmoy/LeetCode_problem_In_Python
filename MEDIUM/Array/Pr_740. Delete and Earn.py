class Solution:
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        
        max_num = max(nums)
        points = [0] * (max_num + 1)
        
        # Step 1: Count points for each number
        for num in nums:
            points[num] += num
        
        # Step 2: House Robber DP
        dp = [0] * (max_num + 1)
        dp[0] = points[0]
        dp[1] = max(points[0], points[1])
        
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + points[i])
        
        return dp[max_num]
