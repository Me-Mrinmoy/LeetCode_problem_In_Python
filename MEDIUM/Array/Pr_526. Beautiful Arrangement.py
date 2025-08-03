class Solution:
    def countArrangement(self, n):
        def backtrack(pos, visited):
            if pos > n:
                return 1

            count = 0
            for i in range(1, n + 1):
                if not visited[i] and (i % pos == 0 or pos % i == 0):
                    visited[i] = True
                    count += backtrack(pos + 1, visited)
                    visited[i] = False
            return count

        visited = [False] * (n + 1)
        return backtrack(1, visited)
