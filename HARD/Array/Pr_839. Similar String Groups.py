class Solution:
    def numSimilarGroups(self, strs):
        n = len(strs)

        # Function to check similarity
        def is_similar(a, b):
            diff = []
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff.append(i)
                if len(diff) > 2:
                    return False
            return len(diff) == 0 or len(diff) == 2

        # DFS to explore groups
        visited = [False] * n

        def dfs(i):
            for j in range(n):
                if not visited[j] and is_similar(strs[i], strs[j]):
                    visited[j] = True
                    dfs(j)

        groups = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                groups += 1
        return groups
