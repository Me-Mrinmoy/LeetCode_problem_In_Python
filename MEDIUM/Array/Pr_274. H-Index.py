class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h += 1
            else:
                break
        return h

# Example usage
sol = Solution()
print(sol.hIndex([3, 0, 6, 1, 5]))  # Output: 3
print(sol.hIndex([1, 3, 1]))        # Output: 1
