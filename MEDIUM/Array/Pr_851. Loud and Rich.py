from collections import defaultdict

class Solution:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = defaultdict(list)
        
        # Build adjacency list (b -> a means a is richer than b)
        for a, b in richer:
            graph[b].append(a)
        
        ans = [-1] * n  # memoization array

        def dfs(x):
            if ans[x] != -1:
                return ans[x]
            
            # Start with themselves
            ans[x] = x
            for nei in graph[x]:
                cand = dfs(nei)
                if quiet[cand] < quiet[ans[x]]:
                    ans[x] = cand
            return ans[x]
        
        # Compute for all people
        for i in range(n):
            dfs(i)
        
        return ans
