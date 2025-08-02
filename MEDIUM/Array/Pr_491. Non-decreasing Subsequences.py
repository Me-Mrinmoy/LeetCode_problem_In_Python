class Solution:
    def findSubsequences(self, nums):
        result = set()
        n = len(nums)

        def dfs(index, path):
            if len(path) >= 2:
                result.add(tuple(path))  # Tuples are hashable for sets

            used = set()
            for i in range(index, n):
                if (not path or nums[i] >= path[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return [list(seq) for seq in result]
