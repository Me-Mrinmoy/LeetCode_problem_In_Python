class Solution:
    def wordBreak(self, s, wordDict):
        # Convert the wordDict list into a set for O(1) lookup
        word_set = set(wordDict)
        
        # DP array where dp[i] is True if s[0:i] can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string can always be segmented

        # Iterate over the string
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If s[j:i] is in the word set and dp[j] is True, set dp[i] to True
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]

# Example usage
solution = Solution()
s = "leetcode"
wordDict = ["leet", "code"]
result = solution.wordBreak(s, wordDict)
print(result)  # Output: True

