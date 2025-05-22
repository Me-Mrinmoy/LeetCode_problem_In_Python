class Solution:
    def permute(self, nums):
        result = []
        self._backtrack(nums, [], result)
        return result

    def _backtrack(self, nums, path, result):
        if len(path) == len(nums):
            result.append(path)
            return
        
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            self._backtrack(nums, path + [nums[i]], result)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1, 2, 3]))
    print(solution.permute([0, 1]))
    print(solution.permute([1]))
