class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n: int = len(nums)
        m: int = 500
        dp: list[dict[int, int]] = [dict() for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i - 1, 0, -1):
                step: int = nums[i - 1] - nums[j - 1]
                dp[i][step] = max(dp[i].get(step, 0), dp[j].get(step, 1) + 1)
        return max(max(chunk.values()) if chunk else 0 for chunk in dp)
