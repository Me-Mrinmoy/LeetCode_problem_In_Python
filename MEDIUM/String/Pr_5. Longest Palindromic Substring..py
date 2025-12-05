class Solution:
    def longestPalindrome(self, s):  # Removed type hints
        if not s:
            return ""

        start, end = 0, 0  # Variables to track the start and end of the longest palindrome

        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)   # Odd-length palindromes
            len2 = self.expandAroundCenter(s, i, i + 1)  # Even-length palindromes
            max_len = max(len1, len2)

            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expandAroundCenter(self, s, left, right):  # Removed type hints
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Length of the palindrome

# Example usage
solution = Solution()
s = "babad"
result = solution.longestPalindrome(s)
print(result)  # Output: "bab" or "aba"
