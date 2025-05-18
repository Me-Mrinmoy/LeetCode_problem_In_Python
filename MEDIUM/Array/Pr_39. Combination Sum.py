class Solution:
    def combinationSum(self, candidates, target):
        result = []
        self.backtrack(candidates, target, [], result, 0)  # start from index 0
        return result

    def backtrack(self, candidates, target, current_combination, result, start):
        if target == 0:
            result.append(list(current_combination))  # Found a valid combination
            return
        if target < 0:
            return  # Exceeded the target

        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])  # Choose the candidate
            self.backtrack(candidates, target - candidates[i], current_combination, result, i)  # Not incrementing i allows for duplicates
            current_combination.pop()  # Backtrack to try another candidate

# Example usage:
solution = Solution()
candidates = [2, 3, 6, 7]
target = 7
output = solution.combinationSum(candidates, target)
print(output)  # Output: [[2, 2, 3], [7]]
