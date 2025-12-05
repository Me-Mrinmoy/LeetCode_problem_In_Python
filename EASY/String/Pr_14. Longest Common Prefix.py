class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Start with the first string as a prefix
        prefix = strs[0]

        for s in strs[1:]:
            # Check how much of the prefix matches with each string
            while s[:len(prefix)] != prefix and prefix:
                # Reduce the prefix by one character from the end
                prefix = prefix[:-1]

        return prefix

# Example usage
sol = Solution()
strs = ["flower", "flow", "flight"]
output = sol.longestCommonPrefix(strs)
print(output)  # Output: "fl"
