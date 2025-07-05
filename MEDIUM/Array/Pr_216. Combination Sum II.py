class Solution:
    def combinationSum3(self, k, n):
        result = []

        def backtrack(start, path, remaining):
            if len(path) == k:
                if remaining == 0:
                    result.append(path[:])
                return

            for i in range(start, 10):  # Numbers from 1 to 9
                if i > remaining:
                    break  # Prune the search if sum exceeds target
                path.append(i)
                backtrack(i + 1, path, remaining - i)
                path.pop()

        backtrack(1, [], n)
        return result


# Example usage:
print(Solution().combinationSum3(3, 7))  # Output: [[1, 2, 4]]
print(Solution().combinationSum3(3, 9))  # Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
print(Solution().combinationSum3(4, 1))  # Output: []
