class Solution:
    def findLength(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max_len = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                else:
                    dp[i][j] = 0
        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.findLength([1,2,3,2,1], [3,2,1,4,7]))  # 3
    print(sol.findLength([0,0,0,0,0], [0,0,0,0,0]))  # 5
