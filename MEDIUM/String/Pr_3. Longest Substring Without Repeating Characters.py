class Solution:
    def lengthOfLongestSubstring(self, s):
        char_index = {}  # Hash map to store the last index of each character
        left = 0  # Left pointer
        max_length = 0  # Variable to store the maximum length of substring

        for right in range(len(s)):
            if s[right] in char_index:
                # Move the left pointer to the right of the last occurrence of s[right]
                left = max(left, char_index[s[right]] + 1)
            
            # Update the last index of the current character
            char_index[s[right]] = right
            
            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length

# Example usage
solution = Solution()
s = "abcabcbb"
result = solution.lengthOfLongestSubstring(s)
print(result)  # Output: 3
